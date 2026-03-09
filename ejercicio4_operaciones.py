def es_primo(numero):

    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_factorial(numero):

    if numero < 0:
        return None 
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

def contar_vocales(texto):
    
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    texto = texto.lower()
    
    for caracter in texto:
        if caracter in vocales:
            vocales[caracter] += 1
    
    return vocales

def main():

    while True:
        print("\n" + "="*50)
        print("MENÚ DE OPERACIONES")
        print("="*50)
        print("1. Determinar si un número es primo")
        print("2. Calcular factorial")
        print("3. Contar vocales en un texto")
        print("4. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':

            print("\nNÚMERO PRIMO")
            while True:
                try:
                    numero = int(input("Ingrese un número entero positivo: "))
                    if numero > 0:
                        break
                    else:
                        print("Error: Ingrese un número positivo")
                except ValueError:
                    print("Error: Ingrese un número entero válido")
            
            if es_primo(numero):
                print(f"El número {numero} SÍ es primo.")
            else:
                print(f"El número {numero} NO es primo.")
        
        elif opcion == '2':
 
            print("\nFACTORIAL")
            while True:
                try:
                    numero = int(input("Ingrese un número entero no negativo: "))
                    if numero >= 0:
                        break
                    else:
                        print("Error: El factorial no está definido para números negativos")
                except ValueError:
                    print("Error: Ingrese un número entero válido")
            
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
        
        elif opcion == '3':

            print("\nCONTADOR DE VOCALES")
            texto = input("Ingrese un texto: ")
            
            if texto.strip():
                conteo = contar_vocales(texto)
                total = sum(conteo.values())
                
                print(f"\nTexto ingresado: '{texto}'")
                print(f"Total de vocales: {total}")
                print("\nDesglose por vocal:")
                for vocal, cantidad in conteo.items():
                    print(f"Vocal '{vocal}': {cantidad}")
            else:
                print("No ingresó ningún texto.")
        
        elif opcion == '4':
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        
        else:
            print("Error: Opción no válida. Por favor seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
