from graphviz import Digraph

def generar_grafica(matriz, nombre_matriz):

    dot = Digraph(comment=nombre_matriz)
    
    # Añadiendo nodos y aristas para representar la matriz
    n = len(matriz)
    m = len(matriz[0]) if n > 0 else 0
    
    for i in range(n):
        for j in range(m):
            if matriz[i][j] != 0:
                dot.node(f'{i+1},{j+1}', f'{matriz[i][j]}')
                if j+1 < m:
                    dot.edge(f'{i+1},{j+1}', f'{i+1},{j+2}')
                if i+1 < n:
                    dot.edge(f'{i+1},{j+1}', f'{i+2},{j+1}')
    
    # Guardar y renderizar el gráfico
    output_path = f'output/{nombre_matriz}'
    dot.render(output_path, format='png', cleanup=True)
    print(f"Gráfico generado exitosamente: {output_path}.png")

# Ejemplo de uso del módulo
if __name__ == "__main__":
    matriz = [[1, 2], [3, 4]]
    generar_grafica(matriz, 'EjemploMatriz')
