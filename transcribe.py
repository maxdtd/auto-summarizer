import warnings
# Ignore pydub ffmpeg warning
#warnings.filterwarnings("ignore")

import os

from datetime import datetime
import speech_recognition as sr 
from pydub import AudioSegment
from pydub.silence import split_on_silence

AUDIO_PATH = 'audio_files\\test.wav'
OUT_FILE = 'hello'

def chunk_on_silence(path):
    audio = AudioSegment.from_wav(path)
    dbfs = audio.dBFS
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=dbfs-16, keep_silence=500)
    # Generate Timestamp
    date_time = datetime.now() #%Y%H%M%S
    time_stamp = date_time.strftime("%d") + date_time.strftime("%m") + date_time.strftime("%Y") + date_time.strftime("%H") + date_time.strftime("%M") + date_time.strftime("%S")
    
    # Create tempoorary storage for chunks
    tmp_dir_name = os.path.join("audio", f"_tmp_{time_stamp}")
    os.mkdir(tmp_dir_name) 

    # Recombine Chunks to have at least 40 seconds in length
    target_length = 40000
    output_chunks = [chunks[0]]
    for chunk in chunks[1:]:
        if len(output_chunks[-1]) < target_length:
            output_chunks[-1] += chunk
        else:
            # if the last output chunk is longer than the target length,
            # we can start a new one
            output_chunks.append(chunk)

    # Export recombined chunks
    i = 0
    for chunk in output_chunks:
        chunk.export(os.path.join(tmp_dir_name, f"chunk{i}.wav"), format="wav")
        print(f"Exported chunk{i}.wav")
        i += 1

    # Open output file
    transcript = open(OUT_FILE, "a+")

    # Recognize Audio and write to transcript
    for file in os.listdir(tmp_dir_name):
        filename = os.path.join(tmp_dir_name, file)
        recognizer = sr.Recognizer()

        with sr.AudioFile(filename) as audio_source:
            recognizer.adjust_for_ambient_noise(audio_source)
            listened_audio = recognizer.listen(audio_source)
        
        try:
            res = recognizer.recognize_google(listened_audio)
            print(res)
            transcript.write(res)
        except sr.UnknownValueError:
            print("Audio is not intelligable!")
        except sr.RequestError as e:
            print(f"Could not request results! Check connection! Error: {e}")

chunk_on_silence(AUDIO_PATH)

"""
TODO: 
    #- pocketsphinx
    #- deepspeech

    - SpeechRecognition API to Google
    - DeepSpeech

    - compare Google to Deepspeech
    - use punctuator

    - test results on 10 minute sample, compare results of deepspeech and google!
    - test results on 10 minute sample lo pass, hi pass, band pass
"""


