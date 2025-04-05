import math
import itertools
import matplotlib.pyplot as plt


def sin_oscillator(freq, amp=1, phase=0, sr=44100):
    increment = 2 * math.pi * freq / sr
    phase_rad = phase * math.pi / 180
    return (amp * math.sin(x + phase_rad) for x in itertools.count(start=0, step=increment))


def plot_signal(signal):
    plt.plot(signal)
    plt.ylabel("amplitude")
    plt.xlabel("sample idx")
    plt.show()


def main():
    osc = sin_oscillator(1, 512)
    samples = [next(osc) for _ in range(512)]

    plot_signal(samples)


if __name__ == "__main__":
    main()
