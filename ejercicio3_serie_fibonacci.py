def main():
    print("SERIE FIBONACCI\n")
    print("La serie comenzará desde 1")

    while True:
        try:
            iteraciones = int(input("Ingrese el número de iteraciones: "))
            
            if iteraciones < 0:
                print("Error: El número de iteraciones no puede ser negativo")
                print("No se generará la serie.")
                return
            elif iteraciones == 0:
                print("No se generarán términos de la serie.")
                return
            else:
                break
        except ValueError:
            print("Error: Ingrese un número entero válido")

    serie = []
    
    if iteraciones >= 1:
        serie.append(1)
    
    if iteraciones >= 2:
        serie.append(1)

    for i in range(2, iteraciones):
        siguiente = serie[i-1] + serie[i-2]
        serie.append(siguiente)

    print("\n" + "="*50)
    print("RESULTADOS DE LA SERIE FIBONACCI")
    print("="*50)
    print(f"Lista completa generada: {serie}")
    print(f"Cantidad de términos generados: {len(serie)}")
    print(f"Último valor incluido: {serie[-1]}")

    print("\n DETALLE DE LA SERIE")
    for i, valor in enumerate(serie, 1):
        print(f"Término {i}: {valor}")

if __name__ == "__main__":
    main()