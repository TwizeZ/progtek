# import numpy as np
# import matplotlib.pyplot as plt
# import scipy as sp

# fs, data = sp.io.wavfile.read('Cdur.wav')
# F = sp.fftpack.fft(data)

# num_samples = len(F)
# sampling_rate = data[0]

# freq_range = np.fft.fftfreq(num_samples, d=1/sampling_rate)

# plt.plot(freq_range, np.abs(F), 'r', label='Fourier transform')
# plt.xlim(0, 2000)

# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('FFT of Audio Signal')
# plt.show()



import numpy as np
import scipy.fftpack
import scipy.io.wavfile
import matplotlib.pyplot as plt

# Read the audio file
sampling_rate, data = scipy.io.wavfile.read('cdur.wav')

# Perform Fourier transform
transformed_data = np.fft.fft(data)

# Find the peaks corresponding to the fundamental frequency (E) and its harmonics
fundamental_frequency = 82.41  # E note frequency in Hz
harmonics_indices = [int(round(i * fundamental_frequency / sampling_rate)) for i in range(1, 9)]  # Up to 8 harmonics
peaks_indices = [np.argmax(np.abs(transformed_data[:len(transformed_data)//2]))] + harmonics_indices

# Move the values in the transformed vector from E to E flat
for peak_index in peaks_indices:
    # Move values to Eb
    transformed_data[peak_index - 4] = transformed_data[peak_index]
    transformed_data[peak_index] = 0  # Zero out the original value
    # Also move values in the mirrored part of the Fourier vector
    transformed_data[-peak_index + 4] = transformed_data[-peak_index]
    transformed_data[-peak_index] = 0  # Zero out the original value

# Plot the transformed data
plt.plot(np.abs(transformed_data[:len(transformed_data)//2]))  # Plot only the positive frequencies
plt.title('Modified Fourier Transformed Data')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.xlim(0, 5000)

# Inverse Fourier transform to get the modified audio signal
modified_data = np.fft.ifft(transformed_data)

# Remove imaginary components and scale to [-1, 1]
modified_data = np.real(modified_data)
modified_data /= np.max(np.abs(modified_data))

plt.plot(modified_data)
plt.show()

# Write the modified audio signal to a WAV file
scipy.io.wavfile.write('Cmin.wav', sampling_rate, modified_data.astype(np.float32))
