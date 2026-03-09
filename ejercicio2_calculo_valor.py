def main():
    print("CÁLCULO DE IMPUESTOS Y DESCUENTOS\n")
    
    while True:
        try:
            valor_base = float(input("Ingrese el valor monetario: $"))
            if valor_base > 0:
                break
            else:
                print("Error: El valor debe ser positivo")
        except ValueError:
            print("Error: Ingrese un número válido")
    
    impuesto = valor_base * 0.19

    if valor_base >= 200000:
        descuento = valor_base * 0.10
    else:
        descuento = 0

    total_final = valor_base + impuesto - descuento

    print("\n" + "="*50)
    print("RESULTADOS")
    print("="*50)
    print(f"Valor base: ${valor_base:,.2f}")
    print(f"Impuesto (19%): ${impuesto:,.2f}")
    print(f"Descuento aplicado: ${descuento:,.2f}")
    print(f"{'Descuento del 10% aplicado' if descuento > 0 else 'No aplica descuento'}")
    print("-"*50)
    print(f"TOTAL FINAL: ${total_final:,.2f}")
    print("="*50)

if __name__ == "__main__":
    main()