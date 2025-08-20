import numpy as np
from src.utils.grapher import graficar_senal

def run():
    # Parámetros
    fs = 256           # Frecuencia de muestreo
    T = 6              # Duración en segundos
    N = fs * T         # Número de muestras
    t = np.arange(N) / fs  # Vector de tiempo discreto

    # Señal original: x[n] = sin(2π*f1*n*Ts) + 0.5*sin(2π*f2*n*Ts)
    f1 = 8
    f2 = 20
    x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

    # Graficar señal original
    graficar_senal(t, x, titulo="Señal original", xlabel="Tiempo [s]", ylabel="Amplitud")

    # DFT de la señal original
    X = np.fft.fft(x)
    freqs = np.fft.fftfreq(N, d=1/fs)
    magnitude = np.abs(X)/N

    # Graficar espectro de la señal original
    graficar_senal(freqs[:N//2], magnitude[:N//2], titulo="DFT de la señal original", xlabel="Frecuencia [Hz]", ylabel="Magnitud")

    # Añadir ruido
    ruido = 0.3 * np.random.randn(N)
    x_ruido = x + ruido

    # Graficar señal con ruido
    graficar_senal(t, x_ruido, titulo="Señal con ruido", xlabel="Tiempo [s]", ylabel="Amplitud")

    # DFT de la señal con ruido
    X_ruido = np.fft.fft(x_ruido)
    magnitude_ruido = np.abs(X_ruido)/N

    # Graficar espectro de la señal con ruido
    graficar_senal(freqs[:N//2], magnitude_ruido[:N//2], titulo="DFT de la señal con ruido", xlabel="Frecuencia [Hz]", ylabel="Magnitud")

if __name__ == "__main__":
    run()
