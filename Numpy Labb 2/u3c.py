import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

fs, data = sp.io.wavfile.read('Cdur.wav')
F = sp.fftpack.fft(data)

num_samples = len(F)
sampling_rate = fs

freq_range = np.fft.fftfreq(num_samples, d=1/sampling_rate)

plt.plot(freq_range, np.abs(F), 'r', label='Fourier transform')

plt.xlim(0, 2000)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT of Audio Signal')
# plt.show()




# --------------------------------------------------------------------------------------------





def frequency_detection(new_freq_range=(80, 100)):
    mask = (freq_range >= new_freq_range[0]) & (freq_range <= new_freq_range[1])
    F_filtered = F[mask]

    freq_range_filtered = freq_range[mask]
    max_freq = freq_range_filtered[np.argmax(np.abs(F_filtered))]
    return max_freq


def overtones():
    e_overtones = []
    freq_range_2 = (320, 340)
    max_freq = frequency_detection(freq_range_2)
    if max_freq:
        for i in range(1, 10):
            overtone_freq = max_freq * i
            print(f"Overtone {i}: {overtone_freq}")
            e_overtones.append(overtone_freq)
    else:
        print("Couldn't find overtone")
    return e_overtones


def major_to_minor(overtones_list):
    new_tones_list = []
    for i, tone in enumerate(overtones_list):
        new_tone = tone * 0.94385432473
        print(f"{i+1}:   Major tone: {tone}      Minor tone: {new_tone}")
        new_tones_list.append(new_tone)
    return new_tones_list


d_sharp_overtones = overtones()
d_minor_overtones = major_to_minor(d_sharp_overtones)


def shift_freq(new_freq_range, target_note):
    # Find the frequency of the note to be shifted
    base_freq = frequency_detection(new_freq_range)

    # Calculate the ratio for frequency shifting
    freq_ratio = target_note / base_freq

    # Perform frequency shifting
    F_shifted = F * freq_ratio
    audio_data_shifted = np.real(sp.fftpack.ifft(F_shifted))

    return audio_data_shifted

def save_wav(audio_file, filename, dtype=np.int16):
    audio_data = audio_file.astype(dtype)
    audio_data_normalized = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)
    sp.io.wavfile.write(filename, fs, audio_data_normalized)


# Example usage:
# Load your audio file
sampling_rate, audio_data = sp.io.wavfile.read('Cdur.wav')
audio_file = (sampling_rate, audio_data)
freq_range_E = (320, 340)

# Define the target frequency for D flat
target_note_D_flat = 288.665

# Shift frequencies corresponding to E to match D flat
audio_file_shifted = shift_freq(freq_range_E, d_sharp_overtones[0])

plt.plot(audio_file_shifted)
plt.show()

# Save the modified audio to a new file
save_wav(audio_file_shifted, 'Cmin.wav')