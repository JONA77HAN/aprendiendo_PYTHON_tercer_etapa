print('Bienvenido al calculador de viáticos')
print('-'*20)
print('1 - Bondi\n2 - Tren\n3 - Subte')

bondi_subte_tren = int(input('Ingrese el medio de transporte: '))

if bondi_subte_tren == 1:
    tarifa_bondi = int(input('¿Qué tarifa abonaste?\n1 - $300\n2 - $325\nIngrese su opción: '))
    if tarifa_bondi == 1:
        costo_viaje = 300
    elif tarifa_bondi == 2:
        costo_viaje = 325
    else:
        print('Opción no válida')
        exit()

elif bondi_subte_tren == 2:
    costo_viaje = 125

elif bondi_subte_tren == 3:
    costo_viaje = 150

else:
    print('Opción no válida')
    exit()

dias_viaje = int(input('¿Cuántos viajes hiciste ? '))
total_gastos = costo_viaje * dias_viaje

print('El total de gastos de viáticos es: $', total_gastos)
