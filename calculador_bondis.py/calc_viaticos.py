suma_monto_bondi = ''

print('bienvenido al calculador de viaticos')
print('-'*20)
print ('1-Bondi \n2-Tren \n3-subte')
bondi_subte_tren = int(input('Ingrese el medio de transporte: '))
if bondi_subte_tren == '1':
    tarifa_bondi = int(input('¿que tarifa abondaste?\n1-$300.-\n2-$325'))
    