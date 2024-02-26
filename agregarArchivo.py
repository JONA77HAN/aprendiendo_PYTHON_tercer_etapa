def agregar_datos_a_archivo(nombre_archivo, datos):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(datos + '\n')

def main():
    print("Bienvenido al programa para agregar datos a un archivo de texto.")
    nombre_archivo = input("Por favor, ingresa el nombre del archivo donde deseas almacenar los datos: ")

    while True:
        datos = input("Ingrese los datos que desea agregar (o 'salir' para finalizar): ")
        if datos.lower() == 'salir':
            print("Saliendo del programa...")
            break
        else:
            agregar_datos_a_archivo(nombre_archivo, datos)
            print("Datos agregados correctamente al archivo.")

if __name__ == "__main__":
    main()
