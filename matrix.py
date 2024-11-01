from lista import ListaEnlazada

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n  
        self.m = m  
        self.filas = ListaEnlazada()
        for _ in range(n):
            fila = ListaEnlazada()
            for _ in range(m):
                fila.agregar(0) 
            self.filas.agregar(fila)

    def agregar_dato(self, x, y, valor):
        try:
            if x < 1 or x > self.n or y < 1 or y > self.m:
                raise IndexError(f"Índice ({x}, {y}) fuera de rango. Tamaño de la matriz: ({self.n}, {self.m})")
            
            fila = self.filas.obtener(x-1) 
            fila.eliminar(y-1) 
            fila.insertar(y-1, valor) 

        except IndexError as e:
            print(f"Error al agregar dato: {e}")
            print("Verifique los índices e intente nuevamente.")

    def obtener_dato(self, x, y):
        try:
            if x < 1 or x > self.n or y < 1 or y > self.m:
                raise IndexError(f"Índice ({x}, {y}) fuera de rango. Tamaño de la matriz: ({self.n}, {self.m})")
            
            fila = self.filas.obtener(x-1) 
            return fila.obtener(y-1) 

        except IndexError as e:
            print(f"Error al obtener dato: {e}")
            print("Verifique los índices e intente nuevamente.")
            return None

    def mostrar_matriz(self):
        for i in range(self.n):
            fila = self.filas.obtener(i) 
            print(fila.mostrar()) 
            


