def validar_nombre(nombre):

    return len(nombre.strip()) >= 3

def validar_edad(edad):

    return 0 <= edad <= 120

def validar_correo(correo):

    correo = correo.lower()
    tiene_arroba = '@' in correo
    tiene_dominio = '.com' in correo or '.edu.co' in correo
    return tiene_arroba and tiene_dominio

def main():

    print("REGISTRO DE USUARIO\n")
    print("Complete el formulario con datos válidos")
    
    lista_usuarios = []
    
    while True:
        print("\n" + "-"*40)
        print("NUEVO REGISTRO")
        print("-"*40)

        while True:
            nombre = input("Nombre (mínimo 3 caracteres): ")
            if validar_nombre(nombre):
                break
            else:
                print("Error: El nombre debe tener al menos 3 caracteres")

        while True:
            try:
                edad = int(input("Edad (entre 0 y 120 años): "))
                if validar_edad(edad):
                    break
                else:
                    print("Error: La edad debe estar entre 0 y 120 años")
            except ValueError:
                print("Error: Ingrese un número entero válido")

        while True:
            correo = input("Correo electrónico (debe contener @ y .com o .edu.co): ")
            if validar_correo(correo):
                break
            else:
                print("Error: El correo debe contener '@' y '.com' o '.edu.co'")

        usuario = {
            "nombre": nombre.strip(),
            "edad": edad,
            "correo": correo.lower().strip()
        }
        
        lista_usuarios.append(usuario)
        print(f"\n✓ Usuario registrado exitosamente: {usuario['nombre']}")

        while True:
            continuar = input("\n¿Desea registrar otro usuario? (s/n): ").lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Error: Ingrese 's' para sí o 'n' para no")
        
        if continuar == 'n':
            break

    if lista_usuarios:
        print("\n" + "="*50)
        print("USUARIOS REGISTRADOS")
        print("="*50)
        
        for i, usuario in enumerate(lista_usuarios, 1):
            print(f"\n--- Usuario #{i} ---")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Edad: {usuario['edad']}")
            print(f"Correo: {usuario['correo']}")
        
        print("\n" + "="*50)
        print(f"Total de usuarios registrados: {len(lista_usuarios)}")
    else:
        print("\nNo se registraron usuarios.")

if __name__ == "__main__":
    main()