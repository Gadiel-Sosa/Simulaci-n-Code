def primaria(semilla, digitos, iteraciones):
    
    valor = str(semilla)
    
    print(f"{'Iteración':<10}{'Valor':<10}{'Cuadrado':<15}{'Nuevo Valor':<10}")
    print("-"*55)
    
    for i in range(1, iteraciones+1):
        
        cuadrado = str(int(valor)**2)
        
        while len(cuadrado) < 2*digitos:
            cuadrado = "0" + cuadrado
            
        inicio = (len(cuadrado) - digitos) // 2
        final = inicio + digitos
        nuevo_valor = cuadrado[inicio:final]
        
        print(f"{i:<10}{valor:<10}{cuadrado:<15}{nuevo_valor:<10}")
        valor = nuevo_valor  
digitos = int(input('Ingresa la cantidad de dígitos de la semilla: '))

while True:
    semilla = int(input('Ingresa una semilla: '))
    if len(str(semilla)) == digitos:
        break
    else:
        print('La semilla no tiene el # de dígitos necesarios')
iteraciones = int(input('Ingresa el # iteraciones totales: '))
primaria(semilla, digitos, iteraciones)