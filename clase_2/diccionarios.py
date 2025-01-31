# estructura de clave: valor

persona = {
    "nombre": "yurley",
    "apellido": "sanchez",
    "trabajos": ["docente", "programadora", "cocinera"],
    "edad": 30
}

alimentos = {
    "frutas": ["manzanas", "kiwi"],
    "verduras": ["espinaca", "ahuyama"],
    "lacteos": ["leche", "queso", "kumis"],
}

"""
persona = [
    "yurley", "sanchez", ["docente", "programadora", "cocinera"], 30
]
"""

print(persona.get("nombre"))
print(alimentos.get("frutas"))
print(alimentos["verduras"])

print(alimentos.get("proteinas"))
# print(alimentos["proteinas"])  <-- FALLA!

"""
1) define un diccionario con informacion personal 
debe contener: (nombre, apellido, hobby, edad )

2) imprimir un mensaje de presentacion usando los valore del diccionario 
declara en el punto 1
"""
