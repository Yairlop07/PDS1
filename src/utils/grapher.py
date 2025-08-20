import matplotlib.pyplot as plt
import numpy as np

# ------------------ Graficar señal continua y discreta juntas ------------------
def graficar_senal(t_cont, x_cont, n_disc=None, x_disc=None, titulo="", xlabel="t", ylabel="x(t)"):
    """
    Grafica una señal continua y, opcionalmente, su versión discreta.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t_cont, x_cont, label="Continuo", color="blue")
    if n_disc is not None and x_disc is not None:
        plt.stem(n_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt="k-", label="Discreto")
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ------------------ Graficar múltiples señales continuas ------------------
def plot_signals(t, signals, labels=None, titulo="", xlabel="t", ylabel="x(t)"):
    """
    Grafica varias señales continuas sobre el mismo gráfico.
    signals: lista de arrays numpy
    labels: lista de nombres de las señales
    """
    plt.figure(figsize=(10, 4))
    for i, x in enumerate(signals):
        label = labels[i] if labels is not None else f"Señal {i+1}"
        plt.plot(t, x, label=label)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ------------------ Graficar señal discreta ------------------
def discrete_plotter(n, x, titulo="", xlabel="n", ylabel="x[n]"):
    """
    Grafica una señal discreta usando stem plot.
    """
    plt.figure(figsize=(10, 4))
    plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt="k-")
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
