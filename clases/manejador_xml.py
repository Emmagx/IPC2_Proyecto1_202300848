import xml.etree.ElementTree as ET

class ManejadorXML:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
    
    def leer_matrices(self):
        try:
            tree = ET.parse(self.archivo_entrada)
            root = tree.getroot()
            matrices = []
            for matriz in root.findall('matriz'):
                nombre = matriz.get('nombre')
                n = int(matriz.find('n').text)
                m = int(matriz.find('m').text)
                nueva_matriz = Matriz(nombre, n, m)
                for dato in matriz.find('datos').findall('dato'):
                    x = int(dato.get('x'))
                    y = int(dato.get('y'))
                    valor = int(dato.text)
                    nueva_matriz.agregar_dato(x, y, valor)
                matrices.append(nueva_matriz)
            return matrices
        except Exception as e:
            print(f"Error leyendo archivo XML: {e}")
            return []

    def escribir_matriz_reducida(self, matriz_reducida):
        try:
            root = ET.Element("matrices")
            matriz_element = ET.SubElement(root, "matriz", nombre=matriz_reducida.nombre)
            n_element = ET.SubElement(matriz_element, "n")
            n_element.text = str(matriz_reducida.n)
            m_element = ET.SubElement(matriz_element, "m")
            m_element.text = str(matriz_reducida.m)
            datos_element = ET.SubElement(matriz_element, "datos")
            for x in range(matriz_reducida.n):
                for y in range(matriz_reducida.m):
                    dato_element = ET.SubElement(datos_element, "dato", x=str(x), y=str(y))
                    dato_element.text = str(matriz_reducida.obtener_dato(x, y))
            tree = ET.ElementTree(root)
            tree.write(self.archivo_salida)
        except Exception as e:
            print(f"Error escribiendo archivo XML: {e}")