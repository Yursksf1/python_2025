"""
hay una serie de palabras --> ejemplo: 
    paises: [colombia, venezuela, argentina, canada, portugal, australia]
    1) seleccionar una de estas palabras
hay que adivinar las letras una por una, hasta adivinar toda la palabra
si falla la letra va a ir dibujando --> descontar intentos
    2) definir un numero de intentos permitidos (6)
    3) pintar la lineas abajo que corresponde a acada letra de la palbra
        ejemplo: colombia --> _ _ _ _ _ _ _ _ 
    4) si acierta una letra se pinta en la posicion correspondiente
        ejemplo: colombia --> o --> _ o _ o _ _ _ _ 
                 colombia --> i --> _ o _ o _ _ i _ 
    5) agregar una validacion de letras que ya fueron usadas (si ya se usaron no deben sumar ni restar intentos)
    6) El juego finaliza cuando se adivina la plabra o se acaben los intentos
"""

import random
palabras = ["colombia", "venezuela", "argentina", "canada", "portugal", "australia"]
letras_usadas = []
num_intentos = 6

palabra = random.choice(palabras)
print(palabra)
guiones = ["_" for _ in range(len(palabra))]

print(" ".join(guiones))
while num_intentos > 0 and palabra != "".join(guiones):
    intento = input("ingresa una letra para adivinar la palabra: ")
    if intento in letras_usadas:
        print("esta letra ya ha sido usada")
    else: 
        letras_usadas.append(intento)
        print(intento)
        if intento in palabra:
            print("la letra que ingresaste se encuentra dentro de la palabra")
        
            for idx, letra in enumerate(palabra):
                if letra == intento:
                    guiones[idx] = intento
                
            print(" ".join(guiones))

        else:
            num_intentos = num_intentos - 1
            print("la letra que ingresaste no se encuentra dentro de la palabra")
            print(f"te quedan {num_intentos} oportunidades")

print('el juego ha finalizado')