from lista import ListaEnlazada

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.filas = ListaEnlazada()
        for _ in range(n):
            fila = ListaEnlazada()
            for _ in range(m):
                fila.agregar(0)  # Inicializa cada fila con 'm' columnas de ceros
            self.filas.agregar(fila)

    def agregar_dato(self, x, y, valor):
        try:
            # Verifica que los índices estén dentro de los límites
            if x < 1 or x > self.n or y < 1 or y > self.m:
                raise IndexError(f"Índice ({x}, {y}) fuera de rango. Tamaño de la matriz: ({self.n}, {self.m})")
            
            fila = self.filas.obtener(x-1)  # Obtén la fila (una lista enlazada)
            fila.eliminar(y-1)  # Elimina el dato anterior en la posición (x, y)
            fila.insertar(y-1, valor)  # Inserta el nuevo valor en la posición correspondiente

        except IndexError as e:
            print(f"Error al agregar dato: {e}")
            print("Verifique los índices e intente nuevamente.")

    def obtener_dato(self, x, y):
        try:
            # Verifica que los índices estén dentro de los límites
            if x < 1 or x > self.n or y < 1 or y > self.m:
                raise IndexError(f"Índice ({x}, {y}) fuera de rango. Tamaño de la matriz: ({self.n}, {self.m})")
            
            fila = self.filas.obtener(x-1)  # Obtén la fila (una lista enlazada)
            return fila.obtener(y-1)  # Devuelve directamente el dato en la posición (x, y)

        except IndexError as e:
            print(f"Error al obtener dato: {e}")
            print("Verifique los índices e intente nuevamente.")
            return None

    def mostrar_matriz(self):
        for i in range(self.n):
            fila = self.filas.obtener(i)  # Obtén la fila (una lista enlazada)
            print(fila.mostrar())  # Muestra la fila completa


