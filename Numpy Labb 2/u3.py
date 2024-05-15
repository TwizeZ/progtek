import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import os


# a


audio_data = sp.io.wavfile.read('Sound/Piano_1_C.wav')
F = sp.fftpack.fft(audio_data[1])

plt.plot(audio_data[1])
plt.show()

plt.plot(F)
plt.show()

sample_rate = audio_data[0]
length = len(F)
freq_range = np.fft.fftfreq(length, 1/sample_rate)

plt.plot(freq_range, np.abs(F))
plt.xlim(0, 10000)

plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.show()


# b


def get_pitch(audio_file):
    F = sp.fftpack.fft(audio_file[1])
    num_samples = len(F)
    sampling_rate = audio_file[0]
    freq_range = np.fft.fftfreq(num_samples, d=1 / sampling_rate)
    max_freq = freq_range[np.argmax(np.abs(F))]

    while max_freq > 500:
        max_freq /= 2

    if 261.6256 - 5 <= max_freq <= 261.6256 + 5:
        return max_freq
    elif 293.6648 - 5 <= max_freq <= 293.6648 + 5:
        return max_freq
    elif 329.6276 - 5 <= max_freq <= 329.6276 + 5:
        return max_freq
    elif 349.2282 - 5 <= max_freq <= 349.2282 + 5:
        return max_freq
    elif 391.9954 - 5 <= max_freq <= 391.9954 + 5:
        return max_freq
    elif 440.0000 - 5 <= max_freq <= 440.0000 + 5:
        return max_freq
    else:
        return max_freq


def get_note(freq):
    freq = freq*2 if freq < 440 else freq
    notes = {
            'A': (440, 466.16),
            'A#': (466.16, 493.88),
            'B': (493.88, 523.25),
            'C': (523.25, 554.37),
            'C#': (554.37, 587.33),
            'D': (587.33, 622.25),
            'D#': (622.25, 659.25),
            'E': (659.25, 698.46),
            'F': (698.46, 739.99),
            'F#': (739.99, 783.99),
            'G': (783.99, 830.61),
            'G#': (830.61, 880)
        }

    for note, (f_min, f_max) in notes.items():
        if f_min <= freq < f_max:
            return note

    return 'Frequency out of range'


freq = get_pitch(audio_data)
print(freq)
note = get_note(freq)
print(note)

sounds = [f for f in os.listdir('Sound') if os.path.isfile(os.path.join('Sound', f))]

for sound in sounds:
    audio_data = sp.io.wavfile.read(f'Sound/{sound}')
    freq = get_pitch(audio_data)
    note = get_note(freq)
    print(f'{sound}: {note}')