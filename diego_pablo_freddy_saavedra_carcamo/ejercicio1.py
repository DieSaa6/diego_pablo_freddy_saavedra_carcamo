cantidad_chefs = 0
while cantidad_chefs <= 0:
    texto = input("¿Cuántos chefs desea registrar?")
    if texto.isdecimal () and int(texto) > 0:
        cantidad_chefs = int(texto)
    else:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")

total_maestros = 0
total_aprendices = 0

for numero_chef in range (1, cantidad_chefs + 1):
    print(f"\nChef {numero_chef}")

    codigo = ""
    while len(codigo) < 6 or " " in codigo:
        codigo = input("Código culinario: ")
        if len(codigo) < 6 or " " in codigo:
            print("Codigo inválido: mínimo 6 caracteres y sin espacios.")

    experiencia = 0
    while experiencia <= 0:
        texto = input("Experiencia culinaria: ")
        if texto.isdecimal() and int(texto) > 0:
            experiencia = int(texto)
        else:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")

    if experiencia > 0:
        total_maestros += 1
    else:
        total_aprendices += 1

print(f"\n¡La escuela cuenta con {total_maestros} Chefs Maestros y {total_aprendices} Chefs Aprendices! ¡A cocinar!")

    