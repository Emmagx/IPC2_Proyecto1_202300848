from lista import *
from matrix import *
class AnalizadorMatrices:
    def __init__(self, matrices):
        self.matrices = matrices
        self.matrices_reducidas = ListaEnlazada()

    def analizar_patrones(self, matriz):
        patrones = {}

        for i in range(matriz.n):
            fila = matriz.filas.obtener(i)
            patron = ''.join(['1' if fila.obtener(j) > 0 else '0' for j in range(matriz.m)])
            if patron not in patrones:
                patrones[patron] = ListaEnlazada()
            patrones[patron].agregar(fila)

        return patrones

    def reducir_matriz(self, matriz):
        patrones = self.analizar_patrones(matriz)
        matriz_reducida = Matriz(nombre=matriz.nombre + "_reducida", n=len(patrones), m=matriz.m)
        i = 0
        for patron, filas in patrones.items():
            nueva_fila = ListaEnlazada()
            for j in range(matriz.m):
                suma = sum(fila.obtener(j) for fila in [filas.obtener(k) for k in range(len(filas))])
                nueva_fila.agregar(suma)
            matriz_reducida.filas.insertar(i, nueva_fila)
            
            print(f"Fila reducida {i}: {nueva_fila.mostrar()}")
            i += 1
        self.matrices_reducidas.agregar(matriz_reducida)

        

    def procesar(self):
        for i in range(len(self.matrices)):
            matriz = self.matrices.obtener(i)
            self.reducir_matriz(matriz)

    def obtener_matrices_reducidas(self):
        print(len(self.matrices_reducidas))
        return self.matrices_reducidas
