import unittest
from clases.manejador_xml import ManejadorXML
from clases.lista_circular import ListaCircular

class TestManejadorXML(unittest.TestCase):

    def test_leer_archivo_xml(self):
        manejador = ManejadorXML("entrada.xml", "salida.xml")
        lista_matrices = manejador.leer_archivo_xml("ruta_del_archivo.xml")
        # Aquí debes verificar el contenido de lista_matrices basado en los datos esperados del archivo XML

    def test_escribir_archivo_xml(self):
        lista = ListaCircular()
        # Añadir algunas matrices a la lista
        manejador = ManejadorXML()
        manejador.escribir_archivo_xml(lista, "salida.xml")
        # Verifica que el archivo salida.xml se haya creado y tenga el contenido correcto

if __name__ == '__main__':
    unittest.main()
