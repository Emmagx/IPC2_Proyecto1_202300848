import unittest
from clases.matrix import Matriz
from clases.grafo import Grafo

class TestGrafo(unittest.TestCase):
    
    def test_agregar_y_verificar_arista(self):
        matriz = Matriz("TestMatriz", 3, 3)
        grafo = Grafo(matriz)
        grafo.agregar_arista("A", "B")
        self.assertTrue(grafo.verificar_arista("A", "B"))
        self.assertFalse(grafo.verificar_arista("A", "C"))

    def test_verificar_nodo(self):
        grafo = Grafo()
        grafo.agregar_arista("A", "B")
        self.assertTrue(grafo.verificar_nodo("A"))
        self.assertTrue(grafo.verificar_nodo("B"))
        self.assertFalse(grafo.verificar_nodo("C"))

    def test_obtener_vecinos(self):
        grafo = Grafo()
        grafo.agregar_arista("A", "B")
        grafo.agregar_arista("A", "C")
        vecinos = grafo.obtener_vecinos("A")
        self.assertIn("B", vecinos)
        self.assertIn("C", vecinos)

if __name__ == '__main__':
    unittest.main()
