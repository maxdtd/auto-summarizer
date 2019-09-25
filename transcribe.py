import warnings
# Ignore pydub ffmpeg warning
#warnings.filterwarnings("ignore")

import os

from datetime import datetime
import speech_recognition as sr 
from pydub import AudioSegment
from pydub.silence import split_on_silence

AUDIO_PATH = 'audio_files\\test.wav'

def chunk_on_silence(path):
    audio = AudioSegment.from_wav(path)
    dbfs = audio.dBFS
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=dbfs-16, keep_silence=500)
    # Generate Timestamp
    date_time = datetime.now() #%Y%H%M%S
    time_stamp = date_time.strftime("%d") + date_time.strftime("%m") + date_time.strftime("%Y") + date_time.strftime("%H") + date_time.strftime("%M") + date_time.strftime("%S")
    
    # Create tempoorary storage for chunks
    tmp_dir_name = os.path.join("audio_files", f"_tmp_{time_stamp}")
    
    os.mkdir(tmp_dir_name) 

    i = 0
    for chunk in chunks:
        chunk.export(os.path.join(tmp_dir_name, f"chunk{i}.wav"), format="wav")
        print(f"Exported chunk{i}.wav")
        i += 1

    for file in os.listdir(tmp_dir_name):
        filename = os.path.join(tmp_dir_name, file)
        recognizer = sr.Recognizer()

        with sr.AudioFile(filename) as audio_source:
            recognizer.adjust_for_ambient_noise(audio_source)
            listened_audio = recognizer.listen(audio_source)
        
        try:
            res = recognizer.recognize_google(listened_audio)
            print(res)
        except sr.UnknownValueError:
            print("Audio is not intelligable!")
        except sr.RequestError as e:
            print("Could not request results! Check connection!")

chunk_on_silence(AUDIO_PATH)

"""
TODO: 
    #- pocketsphinx
    #- deepspeech
    #- wav2letter
    #- julius speech
    #- Kaldi ASR (pykaldi)

    - SpeechRecognition API to Google
    - DeepSpeech

    - compare Google to Deepspeech
    - use punctuator

    - test results on 10 minute sample, compare results of deepspeech and google!
    - test results on 10 minute sample lo pass, hi pass
"""


