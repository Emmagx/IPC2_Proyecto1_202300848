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

    def crear_matriz_accesos(self, matriz):
        matriz_accesos = Matriz(nombre=matriz.nombre + "_accesos", n=matriz.n, m=matriz.m)
        for i in range(matriz.n):
            fila = matriz.filas.obtener(i)
            nueva_fila = ListaEnlazada()
            for j in range(matriz.m):
                valor = 1 if fila.obtener(j) > 0 else 0
                nueva_fila.agregar(valor)
            matriz_accesos.filas.insertar(i, nueva_fila)
        return matriz_accesos

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
            i += 1
        self.matrices_reducidas.agregar(matriz_reducida)

    def procesar(self):
        for i in range(len(self.matrices)):
            matriz = self.matrices.obtener(i)
            matriz_accesos = self.crear_matriz_accesos(matriz)
            self.matrices_reducidas.agregar(matriz)
            self.matrices_reducidas.agregar(matriz_accesos)
            self.reducir_matriz(matriz)

    def obtener_matrices_reducidas(self):
        return self.matrices_reducidas