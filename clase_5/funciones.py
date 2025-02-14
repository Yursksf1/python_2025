def saludo():
    print("hola mundo")

def get_my_name():
    return "Yurley K Sanchez"

def get_new_name():
    new_name = input("Ingresa tu nombre: ")
    return new_name

def saludar(nombre):
    print(f"hola {nombre}")


def saludar_2(nombre):
    return f"hola {nombre}"

saludo()

my_name = get_my_name()
print('my_name:', my_name)

new_name = get_new_name()
print('new_name1:', new_name)

saludar(my_name)
saludar(new_name)

saludo_ma = saludar_2("Maria antonia")
print(saludo_ma)

# Generando errores...
saludar_2(1)
print('esto fallo ')