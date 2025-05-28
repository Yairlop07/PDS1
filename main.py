from src.tarea1 import x1_sin, x2_exp, x3_tri, x4_sq
from src.utils.grapher import graficar_senal

def main():
    # Parámetros
    f = 2       # Frecuencia recomendada
    T_s = 0.01  # Periodo de muestreo

    # Graficar señales
    graficar_senal(x1_sin, f=f, T_s=T_s, nombre="x₁(t) = sin(2π·f·t)")
    graficar_senal(x2_exp, T_s=T_s, nombre="x₂(t) = e^(–2t)·u(t)")
    graficar_senal(x3_tri, f=f, T_s=T_s, nombre="x₃(t) = Señal triangular")
    graficar_senal(x4_sq, f=f, T_s=T_s, nombre="x₄(t) = Señal cuadrada")

if __name__ == "__main__":
    main()
