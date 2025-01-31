# Lista []

nombres = ["juan", "andres", "camilo", "cristina", "maria"]
print(nombres)

print(nombres[3].upper())

print("Hola {}".format(nombres[0]))
print("Hola {}".format(nombres[1]))
print("Hola {}".format(nombres[2]))
print("Hola {}".format(nombres[3]))
print("Hola {}".format(nombres[4]))

# agregar elementos

nombres.append("mateo")
nombres.append("fernando")
nombres.append("lorena")

# eliminar 
nombres.remove('andres')
print(nombres)


# la longitud de la lisata
logitud = len(nombres)
print('la longitud de la lista de nombres es:', logitud)

#una forma de acceder al ultimo elemento de la lista
print(nombres[-1])

# ordenar 
print("sin orden: ", nombres)

nombres.sort()
print("con orden: ", nombres)



# Ejercicio:
"""
crea una lista de frutas
ejemplo: manzana, pera, patilla, uva etc

1.1 1imprime la longitud de la lista creada (len)
1.2 imprime un mensaje que diga: "a mi me gusta comer {} en las tardes" con el indice correspondiente
1.3 imprime un mensaje que diga: "mi fruta favorita es: {}" con el indice correspondiente
1.4 Agrega 3 elementos mas a la lista de frutas que definiste inicialmente
1.5 elimina 2 registros de las frutas que se habian definido inicialmente 
1.6 ordenar de forma alfabetica la lista de frutas 
"""
