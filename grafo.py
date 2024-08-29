from graphviz import Digraph

class Grafo:
    def __init__(self, matriz):
        self.matriz = matriz
        self.grafo = Digraph(format='png')
        self.grafo.attr(rankdir='TB')  # Configurar dirección del grafo de arriba hacia abajo
        self.crear_nodos_matriz()  # Crear nodos y aristas al inicializar

    def crear_nodos_matriz(self):
        # Nodo raíz para la matriz
        self.grafo.node(self.matriz.nombre, shape='ellipse', style='bold')

        # Nodos para m y n con un enlace a la raíz
        self.grafo.node('m', 'm = {}'.format(self.matriz.m), shape='ellipse', color='blue', style='bold')
        self.grafo.node('n', 'n = {}'.format(self.matriz.n), shape='ellipse', color='blue', style='bold')
        self.grafo.edge(self.matriz.nombre, 'm')
        self.grafo.edge(self.matriz.nombre, 'n')

        # Nodos para las filas y los datos
        for i in range(self.matriz.n):
            fila_id = f'Fila {i+1}'
            self.grafo.node(fila_id, fila_id, shape='ellipse', style='bold')
            self.grafo.edge(self.matriz.nombre, fila_id)
            
            fila = self.matriz.filas.obtener(i)
            for j in range(self.matriz.m):
                dato = fila.obtener(j)
                nodo_id = f'{fila_id}_dato_{j+1}'
                self.grafo.node(nodo_id, str(dato), shape='ellipse')

                # Asegurar la alineación vertical de los datos de la misma columna
                if j == 0:
                    # Primera columna se enlaza directamente a la fila
                    self.grafo.edge(fila_id, nodo_id)
                else:
                    # Columnas siguientes se enlazan al nodo anterior de la misma fila
                    nodo_anterior_id = f'{fila_id}_dato_{j}'
                    self.grafo.edge(nodo_anterior_id, nodo_id)

        # Establecer nodos en el mismo rango para mantener la alineación
        with self.grafo.subgraph() as s:
            s.attr(rank='same')
            s.node('m')
            s.node('n')

    def mostrar_grafo(self):
        # Renderiza y visualiza el grafo
        self.grafo.render('grafo_matriz', format='png', cleanup=False)
        self.grafo.view()
