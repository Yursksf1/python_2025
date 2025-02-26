def ingresa_numero():
    try:
        numero = int(input("ingresa un numero: "))
    except Exception as e:
        print(e)
        print("a ocurrido un error, vamos a ingresar el valor por defeto de 0")
        numero = 0
    return numero

numero_1 = ingresa_numero()
numero_2 = ingresa_numero()
print(numero_1 - numero_2)