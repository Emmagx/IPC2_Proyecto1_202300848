class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamaño += 1

    def obtener(self, indice):
        actual = self.cabeza
        contador = 0
        while actual:
            if contador == indice:
                return actual.dato  # Devuelve el dato, no el nodo completo
            actual = actual.siguiente
            contador += 1
        raise IndexError("Índice fuera de rango")


    def eliminar(self, indice):
        if indice == 0:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        contador = 0
        while actual:
            if contador == indice - 1:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
            contador += 1
        raise IndexError("Índice fuera de rango")

    def insertar(self, indice, dato):
        nuevo_nodo = Nodo(dato)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        contador = 0
        while actual:
            if contador == indice - 1:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
            contador += 1
        raise IndexError("Índice fuera de rango")

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos)
    
    def __len__(self):
        return self.tamaño 
