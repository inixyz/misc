import math
import itertools
import matplotlib.pyplot as plt


class SineOscillator:
    def __init__(self, start_freq, start_amp=1, start_phase=0, sr=44100):
        self.start_freq = self.freq = start_freq
        self.start_amp = self.amp = start_amp
        self.start_phase = self.phase = start_phase
        self.sr = sr
        self.x = 0

    def __next__(self):
        increment = 2 * math.pi * self.freq / self.sr
        phase_rad = self.phase * math.pi / 180

        val = math.sin(self.x + phase_rad)
        self.x += increment
        return self.amp * val


def plot_signal(signal):
    plt.plot(signal)
    plt.ylabel("amplitude")
    plt.xlabel("sample idx")
    plt.show()


def main():
    osc = SineOscillator(1)
    samples = [next(osc) for _ in range(44100)]
    plot_signal(samples)


if __name__ == "__main__":
    main()
