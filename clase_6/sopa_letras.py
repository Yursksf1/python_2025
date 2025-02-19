import random 
def create_matrix(elemento, palabra, filas, columnas):
    opciones = ["p", "l", "a", "b", "r"]
    matriz = [[(random.choice(opciones)) for _ in range(columnas)] for _ in range(filas)]
    r_col = random.randint(0,columnas-1-len(palabra))
    r_fil = random.randint(0,filas-1-len(palabra))

    contador_col = r_col
    contador_fil = r_fil
    for p in palabra:
        if False: # case horizontal
            matriz[r_fil][contador_col] = p
            contador_col=contador_col+1
        elif True: # case vertical
            matriz[contador_fil][r_col] = p
            contador_fil = contador_fil+1 # your code is here
        
        elif False: # case diagonal
            matriz[contador_fil][contador_col] = p
            contador_col=contador_col+1
            contador_fil=contador_fil+1
        
    return matriz

def imprime_matrix(matriz):
    for fila in matriz:
        print(fila)

juego = create_matrix("A", "palabra", 10, 15)
imprime_matrix(juego)