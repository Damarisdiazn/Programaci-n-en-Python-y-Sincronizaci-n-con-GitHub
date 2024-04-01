# Crear y escribir en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    file.write("Notas Personales:\n")
    file.write("1. Comprar leche y pan.\n")
    file.write("2. Llamar a Juan para confirmar cita.\n")

# Abrir y leer el archivo línea por línea
with open("my_notes.txt", "r") as file:
    print("Contenido de my_notes.txt:")
    for line in file.readlines():
        # Mostrar cada línea en la consola
        print(line.strip())  # strip() elimina espacios en blanco y saltos de línea adicionales

# Cerrar el archivo automáticamente al salir del bloque "with"
0

