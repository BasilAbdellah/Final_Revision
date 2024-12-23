import numpy as np
from scipy.io import wavfile
from scipy.signal import wiener

fs,noise = wavfile.read("noisy_audio_Final.wav")

noise = noise / np.max(np.abs(noise))

filtered_audio =  wiener(noise,noise=0.1)

filtered_audio = (filtered_audio * 32767).astype(np.int16)

wavfile.write("done.wav",fs,filtered_audio)