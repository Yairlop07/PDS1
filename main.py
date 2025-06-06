import sys
import numpy as np
from src.utils.grapher import graficar_senal
from src.tarea_1 import x1_sin, x2_exp, x3_tri, x4_sq
from src.tarea_2 import generar_senoidal
from src.tarea_3 import ejecutar_tarea_3
from src.tarea_4 import ejecutar_tarea_4

if len(sys.argv) < 2:
    print("Uso: python main.py <tarea> [parametros]")
    sys.exit(1)

tarea = sys.argv[1]

if tarea == "tarea_1":
    print("Ejecutando TAREA 1...")

    t_ini, t_fin = -1, 5
    t_cont = np.linspace(t_ini, t_fin, 1000)
    Ts = 0.01
    n_disc = np.arange(t_ini, t_fin, Ts)

    graficar_senal(t_cont, x1_sin(t_cont), n_disc, x1_sin(n_disc),
                   "Señal 1: Senoidal", "t [s]", "x₁(t)")
    graficar_senal(t_cont, x2_exp(t_cont), n_disc, x2_exp(n_disc),
                   "Señal 2: Exponencial con escalón", "t [s]", "x₂(t)")
    graficar_senal(t_cont, x3_tri(t_cont), n_disc, x3_tri(n_disc),
                   "Señal 3: Triangular", "t [s]", "x₃(t)")
    graficar_senal(t_cont, x4_sq(t_cont), n_disc, x4_sq(n_disc),
                   "Señal 4: Cuadrada", "t [s]", "x₄(t)")

elif tarea == "tarea_2":
    if len(sys.argv) != 3:
        print("Uso: python main.py tarea_2 <frecuencia>")
        sys.exit(1)
    try:
        f = float(sys.argv[2])
    except ValueError:
        print("La frecuencia debe ser un número.")
        sys.exit(1)

    print(f"Ejecutando TAREA 2 con frecuencia f = {f} Hz...")
    t, x = generar_senoidal(f)
    graficar_senal(t, x, None, None,
                   f"Señal Senoidal: f = {f} Hz", "t [s]", "x(t)")

elif tarea == "tarea_3":
    if len(sys.argv) != 5:
        print("Uso: python main.py tarea_3 <amplitud> <frecuencia> <fase>")
        sys.exit(1)
    try:
        A = float(sys.argv[2])
        f = float(sys.argv[3])
        phi = float(sys.argv[4])
    except ValueError:
        print("Todos los parámetros deben ser numéricos.")
        sys.exit(1)

    print(f"Ejecutando TAREA 3 con A = {A}, f = {f}, ϕ = {phi} rad...")
    ejecutar_tarea_3(A, f, phi)

elif tarea == "tarea_4":
    if len(sys.argv) != 3:
        print("Uso: python main.py tarea_4 <n_bits>")
        sys.exit(1)

    try:
        n_bits = int(sys.argv[2])
    except ValueError:
        print("El número de bits debe ser un entero.")
        sys.exit(1)

    print(f"Ejecutando TAREA 4 con {n_bits} bits...")
    ejecutar_tarea_4(n_bits)

else:
    print(f"Tarea desconocida: {tarea}")
