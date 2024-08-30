from lectorXML import *
from analizador import *
from escrituraXML import *
from grafo import *
from ListaGrafo import *
from graphviz import Digraph
class Menu:
    def __init__(self):
        self.lector_xml = None
        self.analizador_matrices = None
        self.escritor_xml = None

    def cargar_archivo(self, ruta):
        self.lector_xml = LectorXML(ruta)
        self.lector_xml.leer()
        print("Archivo cargado exitosamente.")
    
    def procesar_archivo(self):
        if self.lector_xml == None:
            print("Primero debes cargar un archivo.")
            return
        self.analizador_matrices = AnalizadorMatrices(self.lector_xml.obtener_matrices())
        self.analizador_matrices.procesar()
        matrices_reducidas = self.analizador_matrices.obtener_matrices_reducidas()
        for i in range(len(matrices_reducidas)):
            matriz = matrices_reducidas.obtener(i)
            print(f"Matriz Reducida {matriz.nombre}:")
            for x in range(matriz.n):
                fila = matriz.filas.obtener(x)
                print(f"Fila {x+1}: {[fila.obtener(y) for y in range(matriz.m)]}")
        print("Archivo procesado exitosamente.")

    def escribir_archivo_salida(self, ruta_salida):
        if self.analizador_matrices == None:
            print("Primero debes procesar un archivo.")
            return
        self.escritor_xml = EscritorXML(self.analizador_matrices.obtener_matrices_reducidas())
        self.escritor_xml.escribir(ruta_salida)
        print("Archivo de salida escrito exitosamente.")

    def generar_grafo(self):
        if self.lector_xml == None:
            print("Primero debes cargar un archivo.")
            return

        matrices_originales = self.lector_xml.obtener_matrices()
        matrices_procesadas = self.analizador_matrices.obtener_matrices_reducidas()

        # Graficar cada matriz individual
        for i in range(len(matrices_originales)):
            matriz = matrices_originales.obtener(i)
            grafo = Grafo(matriz)
            grafo.guardar_grafo()

        for i in range(len(matrices_procesadas)):
            matriz = matrices_procesadas.obtener(i)
            grafo = Grafo(matriz)
            grafo.guardar_grafo()

        # Graficar la lista circular de matrices
        lista_grafo = ListaGrafo(matrices_procesadas)
        lista_grafo.guardar_grafo()
        print("Grafos generados exitosamente.")