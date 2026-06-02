# problema3.py
# Interpolación Cuadrática - Ejercicio 1

def lagrange(x_puntos, y_puntos, x_eval):
    n = len(x_puntos)
    resultado = 0.0
    for i in range(n):
        termino = y_puntos[i]
        for j in range(n):
            if i != j:
                termino = termino * (x_eval - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        resultado += termino
    return resultado

# Datos del problema - interpolación cuadrática (3 puntos)
x_datos = [1, 4, 7]
y_datos = [3, 24, 67]
x_objetivo = 5

y_final = lagrange(x_datos, y_datos, x_objetivo)

print("=== Interpolación Cuadrática - Problema 1 ===")
print(f"Puntos (x, y): {list(zip(x_datos, y_datos))}")
print(f"Evaluando en x = {x_objetivo}")
print(f"Resultado: y = {y_final:.2f}")
