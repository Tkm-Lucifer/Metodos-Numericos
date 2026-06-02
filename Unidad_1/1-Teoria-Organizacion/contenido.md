# Análisis de Errores Numéricos en Computación

Este documento estudia los errores que ocurren al procesar información matemática en computadoras, derivados de las limitaciones del hardware y el estándar IEEE 754.

---

## 1. Acumulación de Errores en Bucles

### Descripción
Cuando una operación con punto flotante se repite miles de veces en un bucle, el pequeño error de cada iteración se acumula hasta volverse significativo.

### Ejemplo
Sumar `0.1` repetidamente produce un residuo de ~`0.00000000000000004` por iteración. En un millón de ciclos, el error total es considerable.

### Solución
Usar `Decimal` (Python) o `BigDecimal` (Java) para aritmética de precisión arbitraria.

---
Código: [Acumulacion_de_erroresEnBucles.py](../3-Codigos/Acumulacion_de_erroresEnBucles.py)

## 2. Cancelación Catastrófica

### Descripción
Restar dos números muy cercanos entre sí provoca pérdida masiva de dígitos significativos, dejando únicamente ruido de redondeo.

### Ejemplo
`1234567890.1234561 - 1234567890.1234560` debería dar `0.0000001`, pero los bits compartidos se cancelan y lo que queda es ruido.

### Solución
Reformular algebraicamente la ecuación para evitar la resta directa (usar conjugados o series de Taylor).

---
Código: [Cancelacion_resta.py](../3-Codigos/Cancelacion_resta.py)

## 3. Conversión Estrecha

### Descripción
Guardar un valor de mayor precisión en un tipo de dato de menor capacidad provoca truncamiento o pérdida de información irrecuperable.

### Ejemplo
Convertir `double` (64 bits) a `int` (32 bits) elimina la parte decimal y posiblemente los bits más significativos.

### Solución
Diseñar el flujo de datos hacia tipos iguales o mayores. Si se requiere conversión estrecha, validar que el valor cabe en el rango destino.

---
Código: [Conversion_estrecha.py](../3-Codigos/Conversion_estrecha.py)

## 4. Desbordamiento Silencioso (Integer Overflow)

### Descripción
Al superar el valor máximo de un entero de 32 bits (2,147,483,647), el número da la vuelta al valor mínimo negativo sin emitir error.

### Ejemplo
Famoso caso: el cohete Ariane 5 (1996) se destruyó a los 37 segundos por un desbordamiento en los datos de orientación.

### Solución
En Python, los enteros crecen dinámicamente. En C/Java, usar `Math.addExact()` o validaciones previas.

---
Código: [Desbordamiento_silencioso.py](../3-Codigos/Desbordamiento_silencioso.py)

## 5. Error de Redondeo Binario

### Descripción
Las computadoras trabajan en base 2, por lo que fracciones como `0.1` no tienen representación binaria exacta finita, generando un residuo de redondeo.

### Ejemplo
`0.1 + 0.2` en Python da `0.30000000000000004` en lugar de `0.3`.

### Solución
Para dinero o exactitud crítica, guardar valores como enteros (centavos en lugar de pesos) y colocar el punto decimal solo al mostrar.

---
Código: [Error_redondeo_binario.py](../3-Codigos/Error_redondeo_binario.py)

## 6. Errores en Comparación de Flotantes

### Descripción
Comparar flotantes con `==` falla porque los cálculos acumulan ruido en los bits menos significativos, haciendo que valores matemáticamente iguales difieran.

### Ejemplo
`0.1 + 0.1 + 0.1 == 0.3` devuelve `False`.

### Solución
Usar tolerancia (épsilon): `abs(a - b) < 1e-9` en lugar de `a == b`.

---
Código: [MetodosNumericos.py](../3-Codigos/MetodosNumericos.py)

## 7. Pérdida de Precisión por Magnitud (Absorción)

### Descripción
Al sumar un número muy grande con uno muy pequeño, los bits del pequeño son desplazados fuera de la memoria disponible y se pierden.

### Ejemplo
`2.11e17 + 1.0` da `2.11e17`. El `1.0` desapareció.

### Solución
Usar el Algoritmo de Suma de Kahan, que guarda el error residual en una variable de compensación para reinyectarlo después.

---
Código: [Perdida_precisionpormagnitud.py](../3-Codigos/Perdida_precisionpormagnitud.py)

