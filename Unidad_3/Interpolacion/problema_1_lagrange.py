def interpolacion_lagrange(x_valores, y_valores, x_objetivo):
    """
    Calcula el valor de 'y' para un 'x_objetivo' usando el método de 
    Interpolación Polinómica de Lagrange.
    """
    resultado_final = 0.0
    n = len(x_valores)
    
    for i in range(n):
        termino_l = y_valores[i]
        for j in range(n):
            if i != j:
                termino_l = termino_l * (x_objetivo - x_valores[j]) / (x_valores[i] - x_valores[j])
        resultado_final += termino_l
        
    return resultado_final

# --- Datos del problema ---
x_puntos = [1, 4, 7]
y_puntos = [3, 24, 67]
x_a_evaluar = 5

# --- Ejecución ---
y_resultado = interpolacion_lagrange(x_puntos, y_puntos, x_a_evaluar)

print("=== Interpolación de Lagrange ===")
print(f"Puntos X: {x_puntos}")
print(f"Puntos Y: {y_puntos}")
print(f"Calculando para x = {x_a_evaluar} ...")
print(f"El valor resultante es y = {y_resultado}")
