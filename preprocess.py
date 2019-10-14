import warnings
warnings.filterwarnings("ignore")

import os
import subprocess

from pydub import AudioSegment
from pydub import scipy_effects

# Declare path to ffmpeg
AudioSegment.ffmpeg = "D:\\Programme\\ffmpeg\\bin"
# File Declaration
print(os.listdir("."))
MP3_FILE = "res\\audio\\original\\sam_harris_original.mp3"

WAV_FILE = "res\\audio\\edited\\wav_sam_harris_16k_mono.wav"

HP_FILE = "res\\audio\\edited\\wav_hp_sam_harris_16k_mono.wav"
LP_FILE = "res\\audio\\edited\\wav_lp_sam_harris_16k_mono.wav"
BP_FILE = "res\\audio\\edited\\wav_bp_sam_harris_16k_mono.wav"

# open MP3 file
audio_file = AudioSegment.from_mp3(MP3_FILE)
print("> successfully opened mp3 file")

# use ffmpeg for conversion to 16 bit & mono channel wav
subprocess.call(f"ffmpeg -i {MP3_FILE} -acodec pcm_s16le -ac 1 -ar 16000 {WAV_FILE}", shell=True)

# Use pydub low pass filter and export
lp_audio = scipy_effects.low_pass_filter(audio_file, 1000)
LP_MP3 = LP_FILE.replace("wav", "mp3")
lp_audio.export(LP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {LP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {LP_FILE}", shell=True)
print("> successfully saved and converted low pass filter")

# Use pydub high pass filter and export 
hp_audio = scipy_effects.high_pass_filter(audio_file, 5000)
HP_MP3 = HP_FILE.replace("wav", "mp3")
hp_audio.export(HP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {HP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {HP_FILE}", shell=True)
print("> successfully saved and converted high pass filter")

# Use pydub bandpass filter and export
bp_audio = scipy_effects.band_pass_filter(audio_file, 1000, 5000)
BP_MP3 = BP_FILE.replace("wav", "mp3")
bp_audio.export(BP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {BP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {BP_FILE}", shell=True)
print("> successfully saved and converted band pass filter")



""" 
TODO:
    - Spectrogram Analysis -> decide frequencies for test cases

    - remove silence to reduce filesize, compress?
    - try noise reduction
    - use high pass filter
    - use low pass filter
    - lower echo
    - try combination
"""