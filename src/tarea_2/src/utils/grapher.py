import numpy as np
import matplotlib.pyplot as plt

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
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt=' ', label="Muestreo")

    plt.title(nombre)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
