class Nodo:
    def __init__(self, matriz):
        self.matriz = matriz
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_matriz(self, matriz):
        nuevo_nodo = Nodo(matriz)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
    
    def buscar_matriz(self, nombre):
        actual = self.cabeza
        if not actual:
            return None
        while True:
            if actual.matriz.nombre == nombre:
                return actual.matriz
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return None
    
    def eliminar_matriz(self, nombre):
        actual = self.cabeza
        anterior = None
        if not actual:
            return False
        while True:
            if actual.matriz.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    while actual.siguiente != self.cabeza:
                        actual = actual.siguiente
                    actual.siguiente = self.cabeza.siguiente
                    self.cabeza = self.cabeza.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def mostrar_matrices(self):
        actual = self.cabeza
        if not actual:
            return
        while True:
            print(f"Matriz: {actual.matriz.nombre}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

