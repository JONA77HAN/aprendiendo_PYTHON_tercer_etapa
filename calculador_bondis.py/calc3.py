def guardar_gastos(dia, gastos):
    with open('registro_gastos.txt', 'a') as archivo:
        archivo.write(f'Día {dia}: ${gastos}\n')

print('Bienvenido al calculador de viáticos')
print('-'*20)
print('1 - Bondi\n2 - Tren\n3 - Subte')

while True:
    bondi_subte_tren = int(input('Ingrese el medio de transporte (o "0" para salir): '))

    if bondi_subte_tren == 0:
        print('Gracias por usar el calculador de viáticos. ¡Hasta luego!')
        break

    elif bondi_subte_tren == 1:
        total_gastos = 0
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
            total_gastos += costo_viaje * cantidad_viajes

    elif bondi_subte_tren == 2:
        cantidad_viajes = int(input('¿Cuántos viajes de tren realizaste? '))
        total_gastos = 125 * cantidad_viajes

    elif bondi_subte_tren == 3:
        cantidad_viajes = int(input('¿Cuántos viajes de subte realizaste? '))
        total_gastos = 150 * cantidad_viajes

    else:
        print('Opción no válida')
        continue

    print('El total de gastos de viáticos es: $', total_gastos)

    guardar_gastos(bondi_subte_tren, total_gastos)
