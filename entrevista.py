
#Definimos una funcion para poder reciclar y optimizar el uso del programa.
def calcular_resultado(n):

    #si n es menor a 10 calculamos factorial
    if n < 10:
        # Calculamos el factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    #Si es 10 o mayor sumamos.
    else:
        # Sumar todos los enteros positivos menores que n
        suma = sum(range(1, n + 1))
        return suma
    
for i in range(20):
    print(calcular_resultado(i)) # Factorial para números menores a 10 y suma de 10 a 20 
                                 # Para probar el funcionamiento del codigo.
                                 # Empieza desde cero.