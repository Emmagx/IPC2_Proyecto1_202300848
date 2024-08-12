def agrupar_matrices(matrices):
    """
    Agrupa matrices que cumplen ciertas condiciones. En este caso, se agrupan matrices
    por su dimensión.

    Args:
        matrices (list): Lista de tuplas donde cada tupla contiene el nombre de la matriz y la matriz como lista de listas.

    Returns:
        list: Lista de matrices agrupadas por dimensión.
    """
    agrupadas = {}
    for nombre, matriz in matrices:
        n = len(matriz)
        m = len(matriz[0])
        if (n, m) not in agrupadas:
            agrupadas[(n, m)] = []
        agrupadas[(n, m)].append((nombre, matriz))
    return list(agrupadas.values())


def sumar_matrices(matriz1, matriz2):
    """
    Suma dos matrices de igual dimensión.

    Args:
        matriz1 (list): Primera matriz (lista de listas) a sumar.
        matriz2 (list): Segunda matriz (lista de listas) a sumar.

    Returns:
        list: La matriz resultante de sumar matriz1 y matriz2.
    """
    if not matriz1 or not matriz2:
        return None
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No se pueden sumar matrices de diferentes dimensiones.")
        return None
    n = len(matriz1)
    m = len(matriz1[0])
    suma = [[matriz1[i][j] + matriz2[i][j] for j in range(m)] for i in range(n)]
    return suma


def multiplicar_matrices(matriz1, matriz2):
    """
    Multiplica dos matrices si las dimensiones son compatibles.

    Args:
        matriz1 (list): Primera matriz a multiplicar.
        matriz2 (list): Segunda matriz a multiplicar.

    Returns:
        list: La matriz resultante de multiplicar matriz1 por matriz2.
    """
    if len(matriz1[0]) != len(matriz2):
        print("No se pueden multiplicar matrices de estas dimensiones.")
        return None
    n = len(matriz1)
    m = len(matriz2[0])
    p = len(matriz2)
    resultado = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado


def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]


# Ejemplo de uso del módulo
if __name__ == "__main__":
    matrices = [("Matriz 1", [[1, 2], [3, 4]]), ("Matriz 2", [[5, 6], [7, 8]]), ("Matriz 3", [[9, 10], [11, 12]])]
    print("Matrices agrupadas:")
    for grupo in agrupar_matrices(matrices):
        print(grupo)

    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[5, 6], [7, 8]]

    print("\nSuma de matrices:")
    print(sumar_matrices(matriz1, matriz2))

    print("\nProducto de matrices:")
    print(multiplicar_matrices(matriz1, matriz2))

    print("\nTransposición de matriz:")
    print(transponer_matriz(matriz1))