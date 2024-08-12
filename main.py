from xml_handler import cargar_archivo_xml, procesar_datos_matriz, escribir_archivo_xml, mostrar_matrices
from graphviz_generator import generar_grafica
from matrix_processor import agrupar_matrices

def menu():
    """
    Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar archivo XML")
        print("2. Procesar matrices")
        print("3. Generar gráfica")
        print("4. Escribir archivo de salida XML")
        print("5. Mostrar matrices cargadas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ruta = input("Ingrese la ruta del archivo XML a cargar: ")
            global root
            root = cargar_archivo_xml(ruta)
            if root:
                print("Archivo XML cargado exitosamente.")
            else:
                print("No se pudo cargar el archivo XML.")
        
        elif opcion == '2':
            if root:
                global matrices
                matrices = procesar_datos_matriz(root)
                matrices = agrupar_matrices(matrices)
                print("Matrices procesadas exitosamente.")
            else:
                print("Por favor, cargue un archivo XML primero.")
        
        elif opcion == '3':
            if matrices:
                for nombre, matriz in matrices:
                    generar_grafica(matriz, nombre)
                print("Gráficas generadas exitosamente.")
            else:
                print("Por favor, procese las matrices primero.")
        
        elif opcion == '4':
            if matrices:
                ruta_salida = input("Ingrese la ruta del archivo XML de salida: ")
                escribir_archivo_xml(matrices, ruta_salida)
            else:
                print("Por favor, procese las matrices primero.")
        
        elif opcion == '5':
            if matrices:
                mostrar_matrices(matrices)
            else:
                print("No hay matrices cargadas para mostrar.")
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    root = None
    matrices = None
    menu()