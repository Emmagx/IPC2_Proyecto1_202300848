import unittest
from clases.patron_acceso import PatronAcceso
from clases.matrix import Matriz

class TestPatronAcceso(unittest.TestCase):
    
    def test_calcular_frecuencia(self):
        matriz = Matriz("MatrizTest", 3, 3)
        matriz.agregar_dato(0, 0, 1)
        matriz.agregar_dato(1, 1, 2)
        matriz.agregar_dato(2, 2, 3)
        
        patron = PatronAcceso()
        patron.agregar_tupla((0, 0))
        patron.agregar_tupla((1, 1))
        patron.agregar_tupla((2, 2))
        
        patron.calcular_frecuencia(matriz)
        self.assertEqual(patron.frecuencia, 6)

if __name__ == '__main__':
    unittest.main()
