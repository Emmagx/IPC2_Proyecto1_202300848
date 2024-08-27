class NodoMatriz:
    def __init__(self, valor=0):
        self.valor = valor
        self.derecha = None
        self.abajo = None

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.cabeza = None
        self.inicializar_matriz()
    
    def inicializar_matriz(self):
        self.cabeza = NodoMatriz()
        fila_actual = self.cabeza
        
        for i in range (self.n):
            nodo_fila = fila_actual
            for j in range (self.m - 1):
                nodo_fila.derecha = NodoMatriz()
                nodo_fila = nodo_fila.derecha
            if i < self.n -1:
                fila_actual.abajo = NodoMatriz()
                fila_actual = fila_actual.abajo        
                    
    def agregar_dato(self, x, y, valor):
        if x >= self.n or y >= self.m:
            raise IndexError("Índice fuera de rango")
        nodo = self._obtener_nodo(x, y)
        nodo.valor = valor
        
    def _obtener_nodo(self, x, y):
        nodo = self.cabeza
        for i in range(x):
            nodo = nodo.abajo
        for j in range(y):
            nodo = nodo.derecha
        return nodo
        
    def imprimir_dato (self):
        for fila in self.datos:
            print(fila)
        