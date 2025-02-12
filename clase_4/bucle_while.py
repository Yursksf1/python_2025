for i in range(10):
    print(i)

contador = 0
while contador<10:
    print(contador)
    contador = contador+1

bandera = True
contador = 0
while bandera:
    print(contador)
    contador = contador+1
    if contador>10:
        bandera = False

contador = 0
while True:
    print(contador)
    contador = contador+1
    if contador>10:
        break
    