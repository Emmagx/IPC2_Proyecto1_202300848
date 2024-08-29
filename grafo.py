from graphviz import Digraph

class Grafo:
    def __init__(self):
        self.dot = Digraph(comment='Matriz de Frecuencia')

    def generar_grafo(self, matriz):
        self.dot.node('Matriz', f'{matriz.nombre}\n{matriz.n}x{matriz.m}')
        
        # Agregar los nodos para las filas y columnas de la matriz
        for i in range(matriz.n):
            for j in range(matriz.m):
                dato = matriz.obtener_dato(i + 1, j + 1)
                node_id = f'{i+1},{j+1}'
                self.dot.node(node_id, str(dato))

        # Conectar los nodos para formar la matriz
        for i in range(matriz.n):
            for j in range(matriz.m):
                if j < matriz.m - 1:
                    self.dot.edge(f'{i+1},{j+1}', f'{i+1},{j+2}')
                if i < matriz.n - 1:
                    self.dot.edge(f'{i+1},{j+1}', f'{i+2},{j+1}')

    def guardar_grafo(self, filename):
        self.dot.render(filename, format='png', cleanup=True)
        print(f'Gráfico guardado como {filename}.png')

    def mostrar_grafo(self):
        # Muestra el grafo en el sistema predeterminado de visualización de imágenes
        self.dot.view()
