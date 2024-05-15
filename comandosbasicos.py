
import subprocess

def ejecutar(comando):
    subprocess.run(comando, shell=True)

while True:
    print("MENU DE OPERACIONES EN UBUNTU")
    print("1. Crear archivo 'promedio.txt'")
    print("2. Crear directorio 'calificaciones'")
    print("3. Crear directorio 'primer_parcial'")
    print("4. Mover archivo 'promedio.txt' a 'primer_parcial'")
    print("5. Navegar al directorio 'calificaciones'")
    print("6. Crear archivo 'comandos.py' en directorio actual")
    print("7. Navegar al directorio 'calificaciones'")
    print("8. Listar contenido del directorio actual")
    print("9. Navegar al directorio 'primer_parcial'")
    print("10. Salir")

    opcion = int(input("Seleccione una opción (1-10): "))

    if opcion == 1:
        ejecutar("touch promedio.txt")
        print("Archivo 'promedio.txt' creado.")

    elif opcion == 2:
        ejecutar("mkdir calificaciones")
        print("Directorio 'calificaciones' creado.")

    elif opcion == 3:
        ejecutar("mkdir primer_parcial")
        print("Directorio 'primer_parcial' creado.")

    elif opcion == 4:
        ejecutar("mv promedio.txt primer_parcial")
        print("Archivo 'promedio.txt' movido a 'primer_parcial'.")

    elif opcion == 5:
        ejecutar("cd calificaciones")

    elif opcion == 6:
        ejecutar("touch comandos.py")
        print("Archivo 'comandos.py' creado en el directorio actual.")

    elif opcion == 7:
        ejecutar("cd calificaciones")

    elif opcion == 8:
        ejecutar("ls")

    elif opcion == 9:
        ejecutar("cd primer_parcial")

    elif opcion == 10:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")
        
 

        
        



    

    
