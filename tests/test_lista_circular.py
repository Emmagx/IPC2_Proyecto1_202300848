import unittest
from clases.lista_circular import ListaCircular
from clases.matrix import Matriz

class TestListaCircular(unittest.TestCase):

    def test_agregar_y_buscar_matriz(self):
        matriz1 = Matriz("Matriz1", 2, 2)
        matriz2 = Matriz("Matriz2", 3, 3)
        
        lista = ListaCircular()
        lista.agregar_matriz(matriz1)
        lista.agregar_matriz(matriz2)
        
        self.assertEqual(lista.buscar_matriz("Matriz1").nombre, "Matriz1")
        self.assertEqual(lista.buscar_matriz("Matriz2").nombre, "Matriz2")
        self.assertIsNone(lista.buscar_matriz("Matriz3"))

    def test_eliminar_matriz(self):
        matriz1 = Matriz("Matriz1", 2, 2)
        matriz2 = Matriz("Matriz2", 3, 3)
        
        lista = ListaCircular()
        lista.agregar_matriz(matriz1)
        lista.agregar_matriz(matriz2)
        
        lista.eliminar_matriz("Matriz1")
        self.assertIsNone(lista.buscar_matriz("Matriz1"))
        self.assertIsNotNone(lista.buscar_matriz("Matriz2"))

if __name__ == '__main__':
    unittest.main()
