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
            nuevo_nodo.siguiente = self.cabeza  # Apunta a sí mismo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  # Cambia el límite del bucle para la lista circular
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza  # Mantén la circularidad
        self.tamaño += 1

    def obtener(self, indice):
        if indice < 0 or indice >= self.tamaño:
            raise IndexError("Índice fuera de rango")
        
        actual = self.cabeza
        contador = 0
        while contador < indice:
            actual = actual.siguiente
            contador += 1
        return actual.dato  # Devuelve el dato, no el nodo completo

    def eliminar(self, indice):
        if indice < 0 or indice >= self.tamaño:
            raise IndexError("Índice fuera de rango")
        
        if indice == 0:
            if self.tamaño == 1:
                self.cabeza = None  # Lista se vuelve vacía
            else:
                actual = self.cabeza
                while actual.siguiente != self.cabeza:
                    actual = actual.siguiente
                actual.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            contador = 0
            while contador < indice - 1:
                actual = actual.siguiente
                contador += 1
            actual.siguiente = actual.siguiente.siguiente
        
        self.tamaño -= 1

    def insertar(self, indice, dato):
        if indice < 0 or indice > self.tamaño:
            raise IndexError("Índice fuera de rango")
        
        nuevo_nodo = Nodo(dato)
        if indice == 0:
            if not self.cabeza:
                self.cabeza = nuevo_nodo
                nuevo_nodo.siguiente = self.cabeza
            else:
                actual = self.cabeza
                while actual.siguiente != self.cabeza:
                    actual = actual.siguiente
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
                actual.siguiente = self.cabeza
        else:
            actual = self.cabeza
            contador = 0
            while contador < indice - 1:
                actual = actual.siguiente
                contador += 1
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamaño += 1

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        if self.cabeza is not None:
            while True:
                elementos.append(str(actual.dato))
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        return " -> ".join(elementos)
    
    def __len__(self):
        return self.tamaño 
