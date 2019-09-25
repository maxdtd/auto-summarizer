import warnings
warnings.filterwarnings("ignore")
import os
from pydub import AudioSegment
from pydub import scipy_effects

# File Declaration
MP3_FILE = "audio_files/test.mp3"
WAV_FILE = "audio_files/test.wav"

# MP3 -> WAV Conversion
audio_file = AudioSegment.from_mp3(MP3_FILE)
audio_file.export(WAV_FILE, bitrate="16k", format="wav")
print("> successfully converted mp3 to wav")

""" 
TODO:
    - remove silence to reduce filesize, compress?
    - try noise reduction
    - use high pass filter
    - use low pass filter
    - lower echo
    - try combination
"""