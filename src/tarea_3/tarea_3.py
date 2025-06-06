import numpy as np
import matplotlib.pyplot as plt

def ejecutar_tarea_3(A, f, phi, Ts=0.01, t_min=0, t_max=2):
    t = np.linspace(t_min, t_max, 1000)
    n = np.arange(t_min, t_max, Ts)

    x_cont = A * np.sin(2 * np.pi * f * t + phi)
    x_ref_cont = np.sin(2 * np.pi * 1 * t)  # Referencia continua

    x_disc = A * np.sin(2 * np.pi * f * n + phi)
    x_ref_disc = np.sin(2 * np.pi * 1 * n)  # Referencia discreta

    plt.figure(figsize=(10, 4))
    plt.plot(t, x_cont, label="Señal continua", color="blue")
    plt.plot(t, x_ref_cont, '--', label="Referencia continua (A=1, f=1Hz, φ=0)", color="gray")
    plt.stem(n, x_disc, linefmt='r-', markerfmt='ro', basefmt='k-', label="Muestreos")
    plt.stem(n, x_ref_disc, linefmt='g--', markerfmt='go', basefmt='k-', label="Muestreos referencia")

    plt.title(f"Señal Senoidal con A={A}, f={f}Hz, φ={phi} rad")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
