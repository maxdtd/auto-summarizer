#import the plt and wavfile modules 
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

file_path = "../res/audio/edited"
file_name = "wav_bill_gross_16k_mono.wav"
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