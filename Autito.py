def autito():
    anio = int(input("Año del auto ?"))
    peso = int(input("Peso del auto (kg) ?"))

    if anio >= 2020:
        cat_anio = "Reciente"
    elif anio >= 2010:
        cat_anio = "intermedio"
    else:
        cat_anio = "Antiguo"

    if peso <= 1000:
        cat_peso = "Ligero"
    elif peso <= 1500:
        cat_peso = "Mediano"
    else:
        cat_peso = "Pesado"

    if cat_anio == "Reciente" and cat_peso == "Pesado":
        print("Precio a pagar: 800$")
    elif cat_anio == "Reciente" and cat_peso == "Mediano":
        print("Precio a pagar: 650$")
    elif cat_anio == "Reciente" and cat_peso == "Ligero":
        print("Precio a pagar: 500$")
    elif cat_anio == "intermedio" and cat_peso == "Pesado":
        print("Precio a pagar: 700$")
    elif cat_anio == "intermedio" and cat_peso == "Mediano":
        print("Precio a pagar: 550$")
    elif cat_anio == "intermedio" and cat_peso == "Ligero":
        print("Precio a pagar: 400$")
    elif cat_anio == "Antiguo" and cat_peso == "Pesado":
        print("Precio a pagar: 500$")
    elif cat_anio == "Antiguo" and cat_peso == "Mediano":
        print("Precio a pagar: 400$")
    elif cat_anio == "Antiguo" and cat_peso == "Ligero":
        print("Precio a pagar: 300$")