def conversion(pais, valor_dolar):
    pesos = input("Ingresa cantidad de pesos: " + pais + ": ")
    pesos = float(pesos)
    #valor_dolar = 19.92
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Dolares = $" + dolares)

menu = """
+++ Conversor de Monedas 💲 +++

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

Elige una opción: """
opcion = input(menu)


if opcion == '1':
    v_dolar = 19.92
    conversion("mexicanos", v_dolar)

elif opcion == '2':
    v_dolar = 70
    conversion("argentinos", v_dolar)

elif opcion == '3':
    v_dolar = 3865
    conversion("colombianos", v_dolar)


else:
    print("Error elección")




