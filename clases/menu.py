class Menu:
    def __init__(self):
        self.lista_matrices = ListaCircular()

    def mostrar_menu(self):
        while True:
            print("1. Cargar Archivo")
            print("2. Procesar Archivo")
            print("3. Escribir Archivo de Salida")
            print("4. Mostrar Datos del Estudiante")
            print("5. Generar Gráfica")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.cargar_archivo()
            elif opcion == '2':
                self.procesar_archivo()
            elif opcion == '3':
                self.escribir_archivo()
            elif opcion == '4':
                self.mostrar_datos_estudiante()
            elif opcion == '5':
                self.generar_graficas()
            elif opcion == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def cargar_archivo(self):
        archivo = input("Ingrese el nombre del archivo XML: ")
        manejador = ManejadorXML(archivo, "salida.xml")
        matrices = manejador.leer_matrices()
        for matriz in matrices:
            self.lista_matrices.agregar_matriz(matriz)
        print("Archivo cargado correctamente.")

    def procesar_archivo(self):
        print("Procesando archivo...")
        # Implementar la lógica para procesar la matriz

    def escribir_archivo(self):
        print("Escribiendo archivo de salida...")
        # Implementar la lógica para escribir la matriz reducida

    def mostrar_datos_estudiante(self):
        print("Nombre: [Tu nombre]")
        print("Carné: [Tu carné]")

    def generar_graficas(self):
        nombre = input("Ingrese el nombre de la matriz para graficar: ")
        matriz = self.lista_matrices.buscar_matriz(nombre)
        if matriz:
            grafo = Grafo(matriz)
            grafo.generar_grafo(f"grafo_{nombre}")
            print(f"Gráfica generada como grafo_{nombre}.pdf")
        else:
            print("Matriz no encontrada.")
