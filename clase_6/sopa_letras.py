import random 
def create_matrix(elemento, palabra, filas, columnas):
    opciones = ["p", "l", "a", "b", "r"]
    matriz = [[(random.choice(opciones)) for _ in range(columnas)] for _ in range(filas)]
    opcion = random.choice(["1", "2", "3","4", "5", "6"])

    r_col = random.randint(0,columnas-1-len(palabra))
    r_fil = random.randint(0,filas-1-len(palabra))
    if opcion in ["4", "5", "6"]:
        r_col = random.randint(0+len(palabra),columnas-1)
        r_fil = random.randint(0+len(palabra),filas-1)
    contador_col = r_col
    contador_fil = r_fil
    for p in palabra:
        if opcion == "1": # case horizontal
            matriz[r_fil][contador_col] = p
            contador_col=contador_col+1
            
        elif opcion == "2": # case vertical
            matriz[contador_fil][r_col] = p
            contador_fil = contador_fil+1 
        
        elif opcion == "3": # case diagonal
            matriz[contador_fil][contador_col] = p
            contador_col=contador_col+1
            contador_fil=contador_fil+1
            
        elif opcion == "4": # case horizontal atras
            matriz[r_fil][contador_col] = p
            contador_col=contador_col-1

        elif opcion == "5": # case vertical arriba
            matriz[contador_fil][r_col] = p
            contador_fil = contador_fil-1 
            
        elif opcion == "6": # case vertical arriba
            matriz[contador_fil][contador_col] = p
            contador_fil = contador_fil-1 
            contador_col=contador_col-1
        
    return matriz

def imprime_matrix(matriz):
    for fila in matriz:
        print(fila)

juego = create_matrix("A", "palabra", 10, 15)
imprime_matrix(juego)