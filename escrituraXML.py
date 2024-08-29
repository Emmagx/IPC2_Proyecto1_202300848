import xml.etree.ElementTree as ET

class EscritorXML:
    def __init__(self, matrices_reducidas):
        self.matrices_reducidas = matrices_reducidas

    def escribir(self, archivo_salida):
        root = ET.Element("matrices")

        for i in range(len(self.matrices_reducidas)):
            matriz = self.matrices_reducidas.obtener(i)
            matriz_element = ET.SubElement(root, "matriz", nombre=matriz.nombre, n=str(matriz.n), m=str(matriz.m))

            for x in range(matriz.n):
                fila = matriz.filas.obtener(x)
                
                print(f"Fila {x+1} de la matriz '{matriz.nombre}': {[fila.obtener(y) for y in range(matriz.m)]}")
                for y in range(matriz.m):
                    dato = fila.obtener(y)
                    print(f"Escribiendo dato en posición ({x+1}, {y+1}): {dato}") 
                    dato_element = ET.SubElement(matriz_element, "dato", x=str(x+1), y=str(y+1))
                    dato_element.text = str(dato)

        tree = ET.ElementTree(root)
        tree.write(archivo_salida, encoding="utf-8", xml_declaration=True)

