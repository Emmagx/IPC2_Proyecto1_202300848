from graphviz import Digraph
class ListaGrafo:
    def __init__(self, matrices):
        self.matrices = matrices
        self.grafo = Digraph(format='png')
        self.grafo.attr(rankdir='LR')  # Configurar dirección del grafo de izquierda a derecha
        self.crear_nodos_lista()

    def crear_nodos_lista(self):
        # Agregar un título al grafo
        self.grafo.node("Matrices", shape='none', label="Lista Circular de Matrices", fontsize='20')

        actual = self.matrices.cabeza
        primero = actual
        if actual is not None:
            while True:
                self.grafo.node(actual.dato.nombre, shape='ellipse', style='filled', color='lightblue')
                
                # Evitar que la matriz se conecte a sí misma
                if actual.dato.nombre != actual.siguiente.dato.nombre:
                    self.grafo.edge(actual.dato.nombre, actual.siguiente.dato.nombre, constraint='true')
                
                actual = actual.siguiente
                if actual == primero:
                    break

        # Cerrar el ciclo del grafo para que sea circular
        if actual is not None and primero.dato.nombre != actual.dato.nombre:
            self.grafo.edge(actual.dato.nombre, primero.dato.nombre)

    def guardar_grafo(self):
        self.grafo.render(f'grafo_lista_matrices', format='png', cleanup=True)
