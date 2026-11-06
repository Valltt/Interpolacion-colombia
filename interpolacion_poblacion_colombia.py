"""
Proyecto Análisis Numérico I
Interpolación de Lagrange y Newton aplicada a la población de Colombia
Datos: población total CENSADA (conteo efectivo) en los censos del DANE.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------- Datos (DANE) ----------------
años = np.array([1964, 1973, 1985, 1993, 2005, 2018], dtype=float)
pob = np.array([17484508, 20666920, 27867326, 33109840, 41468384, 44164417], dtype=float)
# Se trabaja en millones y con t = año - 1964 para mejorar el condicionamiento
t = años - 1964
y = pob / 1e6

# ---------------- Lagrange ----------------
def lagrange(x, y, xi):
    total = 0.0
    for i in range(len(x)):
        L = 1.0
        for j in range(len(x)):
            if j != i:
                L *= (xi - x[j]) / (x[i] - x[j])
        total += y[i] * L
    return total

# ---------------- Newton ----------------
def dif_divididas(x, y):
    n = len(x)
    T = np.zeros((n, n))
    T[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            T[i, j] = (T[i+1, j-1] - T[i, j-1]) / (x[i+j] - x[i])
    return T

def newton(x, T, xi):
    c = T[0, :]
    res, prod = c[0], 1.0
    for k in range(1, len(x)):
        prod *= (xi - x[k-1])
        res += c[k] * prod
    return res

tabla = dif_divididas(t, y)
print("Coeficientes de Newton (diferencias divididas, primera fila):")
print(np.array2string(tabla[0], precision=8))

# ---------------- Estimaciones en años intermedios ----------------
print("\nEstimación de la población (millones)")
print(f"{'Año':>6} {'Lagrange':>12} {'Newton':>12} {'Lineal a trozos':>16}")
for a in [1970, 1980, 1990, 2000, 2010, 2015]:
    ti = a - 1964
    pl, pn = lagrange(t, y, ti), newton(t, tabla, ti)
    lin = np.interp(ti, t, y)
    print(f"{a:>6} {pl:12.4f} {pn:12.4f} {lin:16.4f}")

# ---------------- Validación: dejar un censo fuera ----------------
print("\nValidación leave-one-out (se omite un censo y se estima)")
print(f"{'Año omitido':>12} {'Real':>9} {'Newton':>9} {'Err rel %':>10} {'Lineal':>9} {'Err rel %':>10}")
for k in range(1, len(t) - 1):          # nodos interiores
    idx = [i for i in range(len(t)) if i != k]
    xs, ys = t[idx], y[idx]
    pn = newton(xs, dif_divididas(xs, ys), t[k])
    lin = np.interp(t[k], xs, ys)
    print(f"{int(años[k]):>12} {y[k]:9.4f} {pn:9.4f} {abs(pn-y[k])/y[k]*100:10.2f} "
          f"{lin:9.4f} {abs(lin-y[k])/y[k]*100:10.2f}")

# ---------------- Gráfica ----------------
tt = np.linspace(0, 54, 400)
yy = [newton(t, tabla, v) for v in tt]
plt.figure(figsize=(8, 4.8))
plt.plot(tt + 1964, yy, label="Polinomio interpolante (grado 5)")
plt.plot(años, y, "--", color="gray", lw=1, label="Interpolación lineal a trozos")
plt.scatter(años, y, color="red", zorder=5, label="Censos DANE (población censada)")
plt.xlabel("Año"); plt.ylabel("Población (millones)")
plt.title("Población de Colombia: interpolación con datos censales")
plt.grid(alpha=.3); plt.legend(); plt.tight_layout()
plt.savefig("grafica_poblacion.png", dpi=150)
