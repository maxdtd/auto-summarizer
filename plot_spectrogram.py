#import the plt and wavfile modules 
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
import argparse

# argparser
parser = argparse.ArgumentParser(description="Plot audio spectrogram for .wav file")
parser.add_argument("audio_file", type=str, help=".wav file path")
args = parser.parse_args()

file_path, file_name = os.path.split(args.audio_file)
file_path = os.path.join(file_path, file_name)

# Read the wav file (mono)
samplingFrequency, signalData = wavfile.read(file_path)

# Plot the signal read from wav file
plt.title(f'Spectrogram of {file_name}')
plt.subplot(111)
plt.specgram(signalData,Fs=samplingFrequency)
plt.magma()
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()