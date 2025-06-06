import matplotlib.pyplot as plt
import numpy as np

def plot_signals(t, signals, labels, title="Señales", xlabel="Tiempo (s)", ylabel="Amplitud"):
    """
    Grafica múltiples señales en una misma figura.
    """
    plt.figure(figsize=(10, 4))
    for x, label in zip(signals, labels):
        plt.plot(t, x, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_senal(t_cont, x_cont, t_disc=None, x_disc=None, titulo="Señal", xlabel="Tiempo", ylabel="Amplitud"):
    """
    Grafica una señal continua y, opcionalmente, su versión discreta.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t_cont, x_cont, label="Señal continua", color="blue")
    if t_disc is not None and x_disc is not None:
        plt.stem(t_disc, x_disc, linefmt="r-", markerfmt="ro", basefmt="k-", label="Señal muestreada")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_comparacion(A, f, phi, Ts=0.01, duracion=2.0):
    """
    Grafica una señal senoidal personalizada junto a una señal de referencia.
    """
    t = np.linspace(0, duracion, 1000)
    n = np.arange(0, duracion, Ts)
    t_disc = n * Ts

    # Señal modificada
    x_mod = A * np.sin(2 * np.pi * f * t + phi)
    x_mod_disc = A * np.sin(2 * np.pi * f * t_disc + phi)

    # Señal de referencia
    x_ref = np.sin(2 * np.pi * 1 * t)
    x_ref_disc = np.sin(2 * np.pi * 1 * t_disc)

    # Gráfica continua
    plt.figure(figsize=(10, 4))
    plt.plot(t, x_mod, label="Señal modificada", color="blue")
    plt.plot(t, x_ref, label="Señal de referencia", linestyle='--', color="gray")
    plt.title("Comparación de señales (continuo)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Gráfica discreta
    plt.figure(figsize=(10, 4))
    plt.stem(t_disc, x_mod_disc, linefmt='b-', markerfmt='bo', basefmt='k-', label="Modificada")
    plt.stem(t_disc, x_ref_disc, linefmt='g--', markerfmt='go', basefmt='k-', label="Referencia")
    plt.title("Comparación de señales (discreto)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
