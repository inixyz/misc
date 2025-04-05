import math
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


class SineOscillator:
    def __init__(self, start_freq, start_amp=1.0, start_phase=0, sr=44100):
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


class SquareOscillator:
    def __init__(self, start_freq, start_amp=1.0, start_phase=0, sr=44100):
        self.start_freq = self.freq = start_freq
        self.start_amp = self.amp = start_amp
        self.start_phase = self.phase = start_phase
        self.sr = sr
        self.x = 0

    def __next__(self):
        increment = 2 * math.pi * self.freq / self.sr
        phase_rad = self.phase * math.pi / 180
        val = 1 if math.sin(self.x + phase_rad) >= 0 else -1
        self.x += increment
        return self.amp * val


def plot_signal(signal):
    plt.plot(signal)
    plt.ylabel("amplitude")
    plt.xlabel("sample idx")
    plt.title("Time Domain Signal")
    plt.grid(True)
    plt.show()


def plot_freq_spectrum(signal, sr):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, d=1 / sr)

    half = N // 2
    freqs = freqs[:half]
    magnitude = np.abs(fft_vals[:half])

    plt.plot(freqs, magnitude)
    plt.title("Magnitude Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def play_signal(signal, sr):
    try:
        print("Playing signal in loop... Press Ctrl+C to stop.")
        while True:
            sd.play(signal, sr, blocking=True)
    except KeyboardInterrupt:
        print("\nStopped playback.")


def main():
    sr = 44100
    osc1 = SineOscillator(440, start_amp=0.5, sr=sr)
    osc2 = SineOscillator(660, start_amp=0.5, sr=sr)
    samples = np.array([(next(osc1) + next(osc2)) / 2 for _ in range(sr)], dtype=np.float32)

    plot_signal(samples)
    plot_freq_spectrum(samples, sr)
    play_signal(samples, sr)


if __name__ == "__main__":
    main()
