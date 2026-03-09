def main():

    print("REGISTRO DE ESTUDIANTE\n")
    
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    
    while True:
        estado = input("Estado (activo/inactivo): ").lower()
        if estado in ["activo", "inactivo"]:
            break
        print("Error: Estado debe ser 'activo' o 'inactivo'")
    
    materias = []
    while len(materias) < 3:
        print(f"\nMateria #{len(materias) + 1}:")
        materia = input("Nombre de la materia: ")
        
        while True:
            try:
                nota = float(input(f"Nota para {materia} (0.0 - 5.0): "))
                if 0.0 <= nota <= 5.0:
                    break
                else:
                    print("Error: La nota debe estar entre 0.0 y 5.0")
            except ValueError:
                print("Error: Ingrese un número válido")
        
        materias.append({
            "nombre": materia,
            "nota": nota
        })
    
    while True:
        opcion = input("\n¿Desea agregar otra materia? (s/n): ").lower()
        if opcion == 's':
            materia = input("Nombre de la materia: ")
            
            while True:
                try:
                    nota = float(input(f"Nota para {materia} (0.0 - 5.0): "))
                    if 0.0 <= nota <= 5.0:
                        break
                    else:
                        print("Error: La nota debe estar entre 0.0 y 5.0")
                except ValueError:
                    print("Error: Ingrese un número válido")
            
            materias.append({
                "nombre": materia,
                "nota": nota
            })
        elif opcion == 'n':
            break
        else:
            print("Error: Ingrese 's' para sí o 'n' para no")
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "estado": estado,
        "materias": [m["nombre"] for m in materias],
        "notas": {m["nombre"]: m["nota"] for m in materias}
    }
    
    print("\n" + "="*50)
    print(f"RESULTADOS PARA: {estudiante['nombre']}")
    print("="*50)
    
    notas_lista = list(estudiante["notas"].values())
    promedio = sum(notas_lista) / len(notas_lista)
    
    mejor_materia = max(estudiante["notas"], key=estudiante["notas"].get)
    mejor_nota = estudiante["notas"][mejor_materia]
    
    peor_materia = min(estudiante["notas"], key=estudiante["notas"].get)
    peor_nota = estudiante["notas"][peor_materia]
    
    aprueba = promedio >= 3.0
    estado_aprobacion = "APRUEBA" if aprueba else "NO APRUEBA"
    
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Estado: {estudiante['estado']}")
    print(f"Materias cursadas: {len(estudiante['materias'])}")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Materia con mejor nota: {mejor_materia} ({mejor_nota:.2f})")
    print(f"Materia con peor nota: {peor_materia} ({peor_nota:.2f})")
    print(f"Resultado final: {estado_aprobacion}")
    
    print("\nDETALLE DE NOTAS")
    for materia, nota in estudiante["notas"].items():
        print(f"{materia}: {nota:.2f}")

if __name__ == "__main__":
    main()