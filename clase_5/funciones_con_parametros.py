def saludar_dia():
    print("hola buenos dias")

def saludar_noche():
    print("hola buenas noches")

def saludar(validar, fun_1, fun_2):
    if validar:
        fun_1()
    else: 
        fun_2()

saludar(False, saludar_dia, saludar_noche)