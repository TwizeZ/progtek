import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# a


sample_rate, audio_data = sp.io.wavfile.read('Sound/Piano_1_C.wav')
F = sp.fftpack.fft(audio_data)

num_samples = len(F)
freq_range = np.fft.fftfreq(num_samples, 1/sample_rate)

def A():
    plt.plot(audio_data)
    plt.plot(F)

    plt.plot(freq_range, np.abs(F))
    plt.xlim(0, 10000)

    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')

    plt.show()


# b


def get_pitch(audio_data, sample_rate):
    F = sp.fftpack.fft(audio_data)
    num_samples = len(F)
    freq_range = np.fft.fftfreq(num_samples, 1/sample_rate)

    max_freq = freq_range[np.argmax(np.abs(F))]

    while max_freq > 500:
        max_freq = max_freq / 2

    if 261.6256 - 5 <= max_freq <= 261.6256 + 5:
        return max_freq, "C"
    elif 277.1826 - 5 <= max_freq <= 277.1826 + 5:
        return max_freq, "C#"
    elif 293.6648 - 5 <= max_freq <= 293.6648 + 5:
        return max_freq, "D"
    elif 311.1270 - 5 <= max_freq <= 311.1270 + 5:
        return max_freq, "D#"
    elif 329.6276 - 5 <= max_freq <= 329.6276 + 5:
        return max_freq, "E"
    elif 349.2282 - 5 <= max_freq <= 349.2282 + 5:
        return max_freq, "F"
    elif 369.9944 - 5 <= max_freq <= 369.9944 + 5:
        return max_freq, "F#"
    elif 391.9954 - 5 <= max_freq <= 391.9954 + 5:
        return max_freq, "G"
    elif 415.3047 - 5 <= max_freq <= 415.3047 + 5:
        return max_freq, "G#"
    elif 440.0000 - 5 <= max_freq <= 440.0000 + 5:
        return max_freq, "A"
    elif 466.1638 - 5 <= max_freq <= 466.1638 + 5:
        return max_freq, "A#"
    else:
        return max_freq, "B"


def B():
    sounds_list = ['Piano_1_C.wav', 'Piano_2.wav', 'Piano_3.wav', 'Piano_4.wav', 'Piano_5.wav', 'Piano_6.wav']
    for sound in sounds_list:
        try:
            new_sample_rate, new_audio_data = sp.io.wavfile.read(f'Sound/{sound}')
            freq = get_pitch(new_audio_data, new_sample_rate)
            print(f'{sound}:   {freq}')
        except:
            print("Make sure the file is in the right location and the name is correct")


# c


def get_note(freq):
    freq = freq*2 if freq < 440 else freq
    notes = {
            'A': (426.92, 453.08),
            'A#': (453.08, 480.8),
            'B': (480.8, 509.08),
            'C': (509.08, 541.29),
            'C#': (541.29, 574.61),
            'D': (574.61, 609.25),
            'D#': (609.25, 645.29),
            'E': (645.29, 682.69),
            'F': (682.69, 721.54),
            'F#': (721.54, 761.83),
            'G': (761.83, 803.61),
            'G#': (803.61, 846.96),
        }

    for note, (f_min, f_max) in notes.items():
        if f_min <= freq < f_max:
            return note

    return 'Frequency out of range'


def C():
    # Reading audio file and getting frequency data
    rate, data = sp.io.wavfile.read('Cdur.wav')
    frequency_data = sp.fftpack.fft(data)

    # Getting the frequency data length and frequency data
    data_length = len(data)
    data_freq = sp.fftpack.fftfreq(int(data_length), 1/rate)

    # Plotting the major
    plt.plot(data_freq, abs(frequency_data), label='major')

    # Getting the indexes of E
    e_index = []
    for i in range(len(frequency_data[0:int(data_length/2)])):
        if abs(frequency_data[i]) > 5e5:
            if get_note(data_freq[i]) == "E":
                e_index.append(i)

    # Getting the indexes of E minor
    c_index_minor = []
    for i in e_index:
        c_index_minor.append(int(i*0.94385432473))

    # Swapping the major to minor
    data_counter = 0
    for i in c_index_minor:
        frequency_data[i] = frequency_data[e_index[data_counter]]
        frequency_data[-i] = frequency_data[-e_index[data_counter]]
        frequency_data[e_index[data_counter]], frequency_data[-e_index[data_counter]] = 0, 0
        
        data_counter += 1

    # Writing the minor to a new audio file
    audio = sp.fftpack.ifft(frequency_data)
    sp.io.wavfile.write('Cmin.wav', rate, audio.astype(np.int16))

    # Plotting the minor
    plt.plot(data_freq, abs(frequency_data), label='minor')
    plt.legend()
    plt.xlim(0, 3000)
    plt.show()

A()
B()
C()