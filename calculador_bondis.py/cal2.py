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
        tarifa_bondi = int(input('¿Qué tarifa abonaste?\n1 - $300\n2 - $325\nIngrese su opción: '))
        if tarifa_bondi == 1:
            costo_viaje = 300
        elif tarifa_bondi == 2:
            costo_viaje = 325
        else:
            print('Opción no válida')
            continue

    elif bondi_subte_tren == 2:
        costo_viaje = 125

    elif bondi_subte_tren == 3:
        costo_viaje = 150

    else:
        print('Opción no válida')
        continue

    dias_viaje = int(input('¿Cuántos días durará su viaje? '))
    total_gastos = costo_viaje * dias_viaje

    print('El total de gastos de viáticos es: $', total_gastos)

    guardar_gastos(dias_viaje, total_gastos)
