from lectorXML import LectorXML
from analizador import AnalizadorMatrices
from escrituraXML import EscritorXML
class Menu:
    def __init__(self):
        self.lector_xml = None
        self.analizador_matrices = None
        self.escritor_xml = None

    def cargar_archivo(self, ruta):
        self.lector_xml = LectorXML(ruta)
        self.lector_xml.leer()
        print("Archivo cargado exitosamente.")

    # def procesar_archivo(self):
    #     if self.lector_xml is None:
    #         print("Primero debes cargar un archivo.")
    #         return
    #     self.analizador_matrices = AnalizadorMatrices(self.lector_xml.obtener_matrices())
    #     self.analizador_matrices.procesar()
    #     print("Archivo procesado exitosamente.")
    
    def procesar_archivo(self):
        if self.lector_xml is None:
            print("Primero debes cargar un archivo.")
            return
        self.analizador_matrices = AnalizadorMatrices(self.lector_xml.obtener_matrices())
        self.analizador_matrices.procesar()
        
        # Verificar el contenido de matrices reducidas antes de proceder
        matrices_reducidas = self.analizador_matrices.obtener_matrices_reducidas()
        for i in range(len(matrices_reducidas)):
            matriz = matrices_reducidas.obtener(i)
            print(f"Matriz Reducida {matriz.nombre}:")
            for x in range(matriz.n):
                fila = matriz.filas.obtener(x)
                print(f"Fila {x+1}: {[fila.obtener(y) for y in range(matriz.m)]}")
        
        print("Archivo procesado exitosamente.")


    def escribir_archivo_salida(self, ruta_salida):
        if self.analizador_matrices is None:
            print("Primero debes procesar un archivo.")
            return
        self.escritor_xml = EscritorXML(self.analizador_matrices.obtener_matrices_reducidas())
        self.escritor_xml.escribir(ruta_salida)
        print("Archivo de salida escrito exitosamente.")
