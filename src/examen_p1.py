import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def run():
    print("Ejecutando examen P1 (DFT)...")
    
    fm = 0.5
    fc = 8
    m = 0.5
    fs = 50
    T = 2
    N = int(fs * T)

    t = np.arange(0, T, 1/fs)
    x = (1 + m * np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)

    continuous_plotter(t, x, title="Señal x(t) - Examen P1")
    discrete_plotter(np.arange(N), x, title="Señal muestreada x[n]")

    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

    X_mag = np.abs(X)/N
    f = np.arange(N) * (fs/N)
    continuous_plotter(f, X_mag, title="Magnitud DFT |X[k]|", xlabel="Frecuencia [Hz]", ylabel="Magnitud")

    peak_threshold = 0.1
    peaks = np.where(X_mag > peak_threshold)[0]
    print("\nPicos espectrales detectados:")
    for k in peaks:
        print(f"Frecuencia: {f[k]:.2f} Hz | Amplitud: {X_mag[k]:.3f}")
