from graphviz import Digraph

class Grafo:
    def __init__(self, matriz):
        self.matriz = matriz
        self.grafo = Digraph(format='png')
        self.grafo.attr(rankdir='TB')  
        self.crear_nodos_matriz() 

    def crear_nodos_matriz(self):
        # Nodo raíz
        self.grafo.node(self.matriz.nombre, shape='ellipse', style='bold')

        # Nodos con un enlace a la raíz
        self.grafo.node('m', 'm = {}'.format(self.matriz.m), shape='ellipse', color='blue', style='bold')
        self.grafo.node('n', 'n = {}'.format(self.matriz.n), shape='ellipse', color='blue', style='bold')
        self.grafo.edge(self.matriz.nombre, 'm')
        self.grafo.edge(self.matriz.nombre, 'n')

        # Nodos para filas y datos
        for i in range(self.matriz.n):
            fila_id = f'Fila {i+1}'
            self.grafo.node(fila_id, fila_id, shape='ellipse', style='bold')
            self.grafo.edge(self.matriz.nombre, fila_id)
            
            fila = self.matriz.filas.obtener(i)
            for j in range(self.matriz.m):
                dato = fila.obtener(j)
                nodo_id = f'{fila_id}_dato_{j+1}'
                self.grafo.node(nodo_id, str(dato), shape='ellipse')

                if j == 0:
                    self.grafo.edge(fila_id, nodo_id)
                else:
                    nodo_anterior_id = f'{fila_id}_dato_{j}'
                    self.grafo.edge(nodo_anterior_id, nodo_id)

        with self.grafo.subgraph() as s:
            s.attr(rank='same')
            s.node('m')
            s.node('n')

    def guardar_grafo(self):
        self.grafo.render(f'grafo_{self.matriz.nombre}', format='png', cleanup=True)
        
