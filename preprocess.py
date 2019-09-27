import warnings
warnings.filterwarnings("ignore")
import os
from pydub import AudioSegment
from pydub import scipy_effects

# File Declaration
MP3_FILE = "D:\\Projekte\\Python\\auto-summarizer\\audio\\original\\tedx_raykurzweil.mp3"
WAV_FILE = "audio\\test.wav"
HP_FILE = "audio\\test_hp.wav"
LP_FILE = "audio\\test_lp.wav"
BP_FILE = "audio\\test_bp.wav"

# open MP3 file
audio_file = AudioSegment.from_mp3(MP3_FILE)

# Use pydub low pass filter and export
lp_audio = audio_file.scipy_effects.low_pass_filter(5000)
lp_audio.export(LP_FILE, bitrate="16k", format="wav")
print("> successfully saved low pass filter")

# Use pydub high pass filter and export 
hp_audio = audio_file.scipy_effects.high_pass_filter(12000)
hp_audio.export(LP_FILE, bitrate="16k", format="wav")
print("> successfully saved high pass filter")

# Use pydub bandpass filter and export
bp_audio = audio_file.scipy_effects.band_pass_filter(5000, 12000)
print("> successfully saved band pass filter")

# MP3 -> WAV Conversion Ouput
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