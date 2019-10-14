#import the pyplot and wavfile modules 
import matplotlib.pyplot as pyplot
from scipy.io import wavfile
import os

file_path = "../res/audio/edited"
file_name = "wav_ray_kurzweil_16k_mono.wav"
file_path = os.path.join(file_path, file_name)

# Read the wav file (mono)
samplingFrequency, signalData = wavfile.read(file_path)

# Plot the signal read from wav file
pyplot.title(f'Spectrogram of {file_name}')

pyplot.subplot(111)

pyplot.specgram(signalData,Fs=samplingFrequency)

pyplot.xlabel('Time')

pyplot.ylabel('Frequency')

pyplot.show()