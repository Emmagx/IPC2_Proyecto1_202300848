from menu import Menu
menu = Menu()

while True:
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Datos del estudiante")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ruta = input("Ingrese la ruta del archivo XML: ")
        menu.cargar_archivo(ruta)
    elif opcion == "2":
        menu.procesar_archivo()
    elif opcion == "3":
        ruta_salida = input("Ingrese la ruta para el archivo de salida XML: ")
        menu.escribir_archivo_salida(ruta_salida)
        
    elif opcion == "4":
        print("Brayan Emanuel Garcia")
        print("Carnet 202300848")
        
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
