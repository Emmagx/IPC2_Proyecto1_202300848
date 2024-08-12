import xml.etree.ElementTree as ET

def cargar_archivo_xml(ruta):

    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Error al cargar el archivo XML: {e}")
        return None


def procesar_datos_matriz(root):
    matrices = []
    
    for matriz in root.findall('matriz'):
        nombre = matriz.get('nombre')
        n = int(matriz.get('n'))
        m = int(matriz.get('m'))
        datos = [[0 for _ in range(m)] for _ in range(n)]
        
        for dato in matriz.findall('dato'):
            x = int(dato.get('x')) - 1  # Ajustar índice a 0
            y = int(dato.get('y')) - 1  # Ajustar índice a 0
            valor = int(dato.text)
            datos[x][y] = valor
        
        matrices.append((nombre, datos))
    
    return matrices


def escribir_archivo_xml(matrices, ruta_salida):
    
    root = ET.Element("matrices")
    
    for nombre, matriz in matrices:
        n = len(matriz)
        m = len(matriz[0]) if n > 0 else 0
        matriz_elem = ET.SubElement(root, "matriz", nombre=nombre, n=str(n), m=str(m))
        
        for i in range(n):
            for j in range(m):
                ET.SubElement(matriz_elem, "dato", x=str(i+1), y=str(j+1)).text = str(matriz[i][j])
    
    tree = ET.ElementTree(root)
    try:
        tree.write(ruta_salida, encoding='utf-8', xml_declaration=True)
        print(f"Archivo XML escrito exitosamente en {ruta_salida}")
    except Exception as e:
        print(f"Error al escribir el archivo XML: {e}")


def mostrar_matrices(matrices):

    for nombre, matriz in matrices:
        print(f"Matriz: {nombre}")
        for fila in matriz:
            print(fila)
        print()


# Ejemplo de uso del módulo
if __name__ == "__main__":
    ruta_entrada = 'resources/input.xml'
    ruta_salida = 'output/output.xml'
    
    # Cargar el archivo XML
    root = cargar_archivo_xml(ruta_entrada)
    
    if root:
        # Procesar las matrices del archivo XML
        matrices = procesar_datos_matriz(root)
        
        # Mostrar matrices en consola
        mostrar_matrices(matrices)
        
        # Escribir las matrices procesadas a un nuevo archivo XML
        escribir_archivo_xml(matrices, ruta_salida)
