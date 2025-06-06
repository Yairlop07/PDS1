import numpy as np
import matplotlib.pyplot as plt

def ejecutar_tarea_4(n_bits):
    """
    Ejecuta la TAREA 4: DAC con n bits.
    """
    VFS = 5.0
    niveles = 2 ** n_bits
    paso = VFS / (niveles - 1)
    resolucion = (paso / VFS) * 100

    print(f"\n--- DAC de {n_bits} bits ---")
    print(f"Niveles totales: {niveles}")
    print(f"Tamaño del paso: {paso:.4f} V")
    print(f"Resolución porcentual: {resolucion:.4f}%")

    entradas_digitales = np.arange(niveles)
    salidas_analogicas = entradas_digitales * paso

    plt.figure(figsize=(8, 4))
    plt.step(entradas_digitales, salidas_analogicas, where='post', color='blue')
    plt.title(f"Salida del DAC de {n_bits} bits")
    plt.xlabel("Entrada digital")
    plt.ylabel("Salida analógica (V)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
