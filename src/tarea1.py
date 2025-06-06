import numpy as np
from scipy.signal import square, sawtooth

def u(t):
    """Función escalón unitario"""
    return np.where(t >= 0, 1, 0)

def x1_sin(t, f=2):
    """Señal sinusoidal: x1(t)"""
    return np.sin(2 * np.pi * f * t)

def x2_exp(t):
    """Señal exponencial: x2(t)"""
    return np.exp(-2 * t) * u(t)

def x3_tri(t, f=2):
    """Señal triangular periódica: x3(t)"""
    return sawtooth(2 * np.pi * f * t, 0.5)

def x4_sq(t, f=2):
    """Señal cuadrada periódica: x4(t)"""
    return square(2 * np.pi * f * t)
