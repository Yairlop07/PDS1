import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth

def u(t):
    """Función escalón unitario"""
    return np.where(t >= 0, 1, 0)

def x1_sin(t, f=2):
    """Señal sinusoidal: x1(t) = sin(2π·f·t)"""
    return np.sin(2 * np.pi * f * t)

def x2_exp(t):
    """Señal exponencial: x2(t) = e^(–2t) · u(t)"""
    return np.exp(-2 * t) * u(t)

def x3_tri(t, f=2):
    """Señal triangular periódica: x3(t)"""
    return sawtooth(2 * np.pi * f * t, 0.5)  # simétrica

def x4_sq(t, f=2):
    """Señal cuadrada: x4(t)"""
    return square(2 * np.pi * f * t)

def graficar_senal(func, f=2, T_s=0.01, nombre="Señal"):
    t_cont = np.linspace(-1, 5, 1000)
    x_cont = func(t_cont, f) if 'f' in func.__code__.co_varnames else func(t_cont)

    # Señal discreta
    n = np.arange(-100, int(5 / T_s))
    t_disc = n * T_s
    x_disc = func(t_disc, f) if 'f' in func.__code__.co_varnames else func(t_disc)

    # Gráfica
    plt.figure(figsize=(10, 4))
    plt.plot(t_cont, x_cont, label="Señal continua", linewidth=2)
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt=' ', label="Muestreo", use_line_collection=True)
    plt.title(nombre)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
