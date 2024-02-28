def mostrar_tarifas_bondi():
    print('Tarifas de Bondi:')
    print('1 - $300')
    print('2 - $325')

def guardar_gastos(dia, gastos):
    with open('registro_gastos.txt', 'a') as archivo:
        archivo.write(f'Día {dia}: ${gastos}\n')

print('Bienvenido al calculador de viáticos')
print('-'*20)
print('1 - Bondi\n2 - Tren\n3 - Subte')

total_gastos = 0

while True:
    medio_transporte = int(input('Ingrese el medio de transporte (o "0" para finalizar y guardar): '))

    if medio_transporte == 0:
        print(f'El total de gastos de viáticos es: ${total_gastos}')
        guardar_gastos('Total', total_gastos)
        print('Gastos guardados en el archivo "registro_gastos.txt"')
        break

    elif medio_transporte == 1:
        mostrar_tarifas_bondi()
        total_gastos_bondi = 0
        while True:
            tarifa_bondi = int(input('¿Qué tarifa abonaste para este viaje de bondi? (Ingrese "0" para finalizar): '))
            if tarifa_bondi == 0:
                break
            elif tarifa_bondi == 1:
                costo_viaje = 300
            elif tarifa_bondi == 2:
                costo_viaje = 325
            else:
                print('Opción no válida')
                continue
            cantidad_viajes = int(input('¿Cuántos viajes realizaste con esta tarifa? '))
            total_gastos_bondi += costo_viaje * cantidad_viajes

        total_gastos += total_gastos_bondi

    elif medio_transporte == 2:
        cantidad_viajes = int(input('¿Cuántos viajes de tren realizaste? '))
        total_gastos += 125 * cantidad_viajes

    elif medio_transporte == 3:
        cantidad_viajes = int(input('¿Cuántos viajes de subte realizaste? '))
        total_gastos += 150 * cantidad_viajes

    else:
        print('Opción no válida')
        continue
