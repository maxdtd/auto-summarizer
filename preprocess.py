import warnings
warnings.filterwarnings("ignore")

import os
import subprocess
import argparse

from pydub import AudioSegment
from pydub import scipy_effects

# Declare path to ffmpeg
# AudioSegment.ffmpeg = "D:\\Programme\\ffmpeg\\bin"
# File Declaration

parser = argparse.ArgumentParser(description="Use filters and create .wav for LP, HP and BP filters")
parser.add_argument("mp3_name", type=str, help="original .mp3 file path")
args = parser.parse_args()

ORIGINAL_PATH = "res/audio/original"
MP3_FILE = os.path.join(ORIGINAL_PATH, args.mp3_name)
FILE_DENOMINATOR = args.mp3_name.split(".")[0]

OUT_PATH = f"res/audio/edited/{FILE_DENOMINATOR}"
WAV_FILE = os.path.join(OUT_PATH,f"{FILE_DENOMINATOR}_16k_mono.wav")

HP_FILE = os.path.join(OUT_PATH,f"hp_{FILE_DENOMINATOR}_16k_mono.wav")
LP_FILE = os.path.join(OUT_PATH,f"lp_{FILE_DENOMINATOR}_16k_mono.wav")
BP_FILE = os.path.join(OUT_PATH,f"bp_{FILE_DENOMINATOR}_16k_mono.wav")

# open MP3 file
audio_file = AudioSegment.from_mp3(MP3_FILE)
print("> successfully opened mp3 file")

# use ffmpeg for conversion to 16 bit & mono channel wav
subprocess.call(f"ffmpeg -i {MP3_FILE} -acodec pcm_s16le -ac 1 -ar 16000 {WAV_FILE}", shell=True)

# Use pydub low pass filter and export
lp_audio = scipy_effects.low_pass_filter(audio_file, 3500)
LP_MP3 = LP_FILE.replace("wav", "mp3")
lp_audio.export(LP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {LP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {LP_FILE}", shell=True)
print("> successfully saved and converted low pass filter")

# Use pydub high pass filter and export 
hp_audio = scipy_effects.high_pass_filter(audio_file, 70)
HP_MP3 = HP_FILE.replace("wav", "mp3")
hp_audio.export(HP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {HP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {HP_FILE}", shell=True)
print("> successfully saved and converted high pass filter")

# Use pydub bandpass filter and export
bp_audio = scipy_effects.band_pass_filter(audio_file, 70, 3500)
BP_MP3 = BP_FILE.replace("wav", "mp3")
bp_audio.export(BP_MP3, format="mp3")
subprocess.call(f"ffmpeg -i {BP_MP3} -acodec pcm_s16le -ac 1 -ar 16000 {BP_FILE}", shell=True)
print("> successfully saved and converted band pass filter")