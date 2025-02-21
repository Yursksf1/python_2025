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

def selecciona_palabra():
    palabras = ["colombia", "venezuela", "argentina", "canada", "portugal", "australia"]
    palabra = random.choice(palabras)
    return palabra

def imprimir_guiones(guiones):
    print(" ".join(guiones))

def validar_intento(intento, palabra, guiones, num_intentos):
    print(intento)
    if intento in palabra:
        print("la letra que ingresaste se encuentra dentro de la palabra")
    
        for idx, letra in enumerate(palabra):
            if letra == intento:
                guiones[idx] = intento
            
        imprimir_guiones(guiones)

    else:
        num_intentos = num_intentos - 1
        print("la letra que ingresaste no se encuentra dentro de la palabra")
        print(f"te quedan {num_intentos} oportunidades")
    return dict(
        intento=intento, 
        palabra=palabra, 
        guiones=guiones, 
        num_intentos=num_intentos
    )

def ingresar_intento(letras_usadas):
    while True:
        intento = input("ingresa una letra para adivinar la palabra: ")
        if intento in letras_usadas:
            print("esta letra ya ha sido usada")
        else: 
            letras_usadas.append(intento)
            return intento

def run():
    letras_usadas = []
    num_intentos = 6
    palabra = selecciona_palabra()
    guiones = ["_" for _ in range(len(palabra))]
    imprimir_guiones(guiones)
    
    while num_intentos > 0 and palabra != "".join(guiones):
        intento = ingresar_intento(letras_usadas)
        data = validar_intento(intento, palabra, guiones, num_intentos)
        intento = data.get("intento") 
        palabra = data.get("palabra")
        guiones = data.get("guiones")
        num_intentos = data.get("num_intentos")

    print('el juego ha finalizado')


if __name__ == "__main__":
    run()