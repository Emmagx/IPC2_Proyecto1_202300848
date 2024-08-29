import xml.etree.ElementTree as ET
from matrix import *
from lista import *
class LectorXML:
    def __init__(self, archivo):
        self.archivo = archivo
        self.matrices = ListaEnlazada()

    def leer(self):
        tree = ET.parse(self.archivo)
        root = tree.getroot()
        for matriz_element in root.findall('matriz'):
            nombre = matriz_element.get('nombre')
            n = int(matriz_element.get('n'))
            m = int(matriz_element.get('m'))
            matriz = Matriz(nombre, n, m)
            for dato_element in matriz_element.findall('dato'):
                x = int(dato_element.get('x'))
                y = int(dato_element.get('y'))
                valor = int(dato_element.text)
                matriz.agregar_dato(x, y, valor)
            self.matrices.agregar(matriz)

    def obtener_matrices(self):
        return self.matrices
