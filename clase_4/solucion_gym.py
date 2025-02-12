def calcular_costo(nombre, horas):
    if 0 < horas <= 15:
        categoria = "Bronce"
        costo = horas * 5000
    elif 15 < horas <= 30:
        categoria = "Plata"
        costo = horas * 3500
    else:
        categoria = "Oro"
        costo = horas * 2000
    return categoria, costo

clientes = [
    {"nombre": "Juan", "horas": 25},
    {"nombre": "Mary", "horas": 10},
    {"nombre": "Daniel", "horas": 35}
]

for cliente in clientes:
    categoria, costo = calcular_costo(cliente["nombre"], cliente["horas"])
    print(f"{cliente['nombre']} estuvo en el gimnasio {cliente['horas']} horas en el mes, categoría {categoria}, por un valor de {costo}")


horas_daniel = 35
categoria_daniel, costo_daniel = calcular_costo("Daniel", horas_daniel)
print(f"Daniel debería pagar {costo_daniel}")