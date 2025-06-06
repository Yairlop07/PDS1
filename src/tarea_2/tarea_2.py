import numpy as np
from src.utils.grapher import plot_signals

def generar_senoidal(frecuencia, A=1, duracion=2.0, muestras=1000):
    """
    Genera una señal senoidal continua: x(t) = A * sin(2πft)
    """
    t = np.linspace(0, duracion, muestras)
    x = A * np.sin(2 * np.pi * frecuencia * t)
    return t, x

def ejecutar_tarea(frecuencia):
    """
    Ejecuta la TAREA 2 graficando una señal senoidal con la frecuencia dada.
    """
    t, x = generar_senoidal(frecuencia)
    plot_signals(t, [x], [f"Señal Senoidal - {frecuencia} Hz"])

def senal_senoidal(f, t):
    A = 1
    return A * np.sin(2 * np.pi * f * t)
