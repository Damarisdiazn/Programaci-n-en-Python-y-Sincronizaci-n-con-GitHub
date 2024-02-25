def ordenar_fila(matriz, fila):
    # Ordenar la fila utilizando el algoritmo de selección
    for i in range(len(matriz[fila])):
        min_idx = i
        for j in range(i+1, len(matriz[fila])):
            if matriz[fila][j] < matriz[fila][min_idx]:
                min_idx = j
        matriz[fila][i], matriz[fila][min_idx] = matriz[fila][min_idx], matriz[fila][i]

# Definir la matriz bidimensional
matriz = [
    [9, 2, 3],
    [4, 5, 1],
    [7, 8, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar (por ejemplo, la primera fila)
fila_a_ordenar = 0

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)