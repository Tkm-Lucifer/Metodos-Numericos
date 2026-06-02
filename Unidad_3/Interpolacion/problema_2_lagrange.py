# problema2.py
# Interpolación de Lagrange - Ejercicio 2

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

# Datos del problema
x_datos = [1, 2, 3]
y_datos = [5, 12, 23]
x_objetivo = 2.5

y_final = lagrange(x_datos, y_datos, x_objetivo)

print("=== Solución al Problema 2 ===")
print(f"Puntos (x, y): {list(zip(x_datos, y_datos))}")
print(f"Evaluando en x = {x_objetivo}")
print(f"Resultado: y = {y_final}")
