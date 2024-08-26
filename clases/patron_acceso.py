class NodoTupla:
    def __init__(self, tupla):
        self.tupla = tupla
        self.siguiente = None

class PatronAcceso:
    def __init__(self):
        self.cabeza = None
        self.frecuencia = 0
    
    def agregar_tupla(self, tupla):
        nuevo_nodo = NodoTupla(tupla)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def calcular_frecuencia(self, matriz):
        actual = self.cabeza
        while actual:
            x, y = actual.tupla
            self.frecuencia += matriz.obtener_dato(x, y)
            actual = actual.siguiente
