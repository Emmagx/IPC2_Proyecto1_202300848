import graphviz

class Grafo:
    def __init__(self, matriz):
        self.matriz = matriz
    
    def generar_grafo(self, nombre_archivo="grafo"):
        dot = graphviz.Digraph(comment=self.matriz.nombre)
        for x in range(self.matriz.n):
            for y in range(self.matriz.m):
                dot.node(f'{x},{y}', label=str(self.matriz.obtener_dato(x, y)))
                if y < self.matriz.m - 1:
                    dot.edge(f'{x},{y}', f'{x},{y+1}')
                if x < self.matriz.n - 1:
                    dot.edge(f'{x},{y}', f'{x+1},{y}')
        dot.render(nombre_archivo)

# Ejemplo de uso:
# grafo = Grafo(matriz)
# grafo.generar_grafo("mi_grafo")
