import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

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

def C():
    rate_upg_c, data_upg_c = sp.io.wavfile.read('Cdur.wav')
    frequency_data = abs(sp.fftpack.fft(data_upg_c))
    length_data_c = len(data_upg_c)
    data_frequency = sp.fftpack.fftfreq(int(length_data_c), 1/rate_upg_c)
    plt.plot(data_frequency, abs(frequency_data), label='major')

    indexes_of_e = []
    for i in range(len(frequency_data[0:int(length_data_c/2)])):
        if frequency_data[i] > 5e5:
            if get_note(data_frequency[i]) == "E":
                indexes_of_e.append(i)

    indexes_of_e_minor = []
    for i in indexes_of_e:
        indexes_of_e_minor.append(int(i*0.94385432473))

    counter = 0
    for i in indexes_of_e_minor:
        frequency_data[i] = frequency_data[indexes_of_e[counter]]
        frequency_data[-i] = frequency_data[-indexes_of_e[counter]]
        frequency_data[indexes_of_e[counter]], frequency_data[-indexes_of_e[counter]] = 0, 0
        
        counter += 1

    audio = sp.fftpack.ifft(frequency_data)

    sp.io.wavfile.write('Cdur_minor.wav', rate_upg_c, audio.astype(np.int16))

    plt.plot(data_frequency, abs(frequency_data), label='minor')
    plt.legend()
    plt.xlim(0, 3000)
    plt.show()

C()