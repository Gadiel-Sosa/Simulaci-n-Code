def cuadrado_medio(semilla, digitos, iteraciones):
    valor = semilla
    print(f"{'Iteración':<10}{'Valor':<10}{'Cuadrado':<20}{'Nuevo valor':<12}")
    print("-" * 52)
    
    for i in range(1, iteraciones + 1):
        # Elevar al cuadrado y rellenar con ceros a la izquierda
        cuadrado = str(valor ** 2).zfill(digitos * 2)
        
        # Calcular posición inicial y final
        inicio = (len(cuadrado) - digitos) // 2
        fin = inicio + digitos
        
        # Extraer dígitos centrales
        nuevo_valor = int(cuadrado[inicio:fin])
        
        # Imprimir fila de la tabla
        print(f"{i:<10}{valor:<10}{cuadrado:<20}{nuevo_valor:<12}")
        
        # Actualizar valor para la siguiente iteración
        valor = nuevo_valor


# Ejemplo de uso
cuadrado_medio(5735, 4, 10)


