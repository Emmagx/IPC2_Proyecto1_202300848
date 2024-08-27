import unittest
from clases.matrix import Matriz

class TestMatriz(unittest.TestCase):
    
    def test_inicializar_matriz(self):
        matriz = Matriz("MatrizTest", 2, 2)
        self.assertEqual(matriz.obtener_dato(0, 0), 0)
        self.assertEqual(matriz.obtener_dato(1, 1), 0)

    def test_agregar_y_obtener_dato(self):
        matriz = Matriz("MatrizTest", 2, 2)
        matriz.agregar_dato(0, 0, 5)
        self.assertEqual(matriz._obtener_nodo(0, 0), 5)
        matriz.agregar_dato(1, 1, 10)
        self.assertEqual(matriz._obtener_nodo(1, 1), 10)
        
    def obtener_dato(self, x, y):
        nodo = self._obtener_nodo(x, y)
        return nodo.valor

if __name__ == '__main__':
    unittest.main()
