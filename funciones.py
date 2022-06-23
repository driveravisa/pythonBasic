# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


#---  Funcion mensaje
# def conversacion(mensaje):
#     print("hola")
#     print("Cómo estás")
#     print(mensaje)
#     print("Adios")

# opcion  = int(input("Elige una opción 1, 2 ó 3 "))

# if opcion == 1:
#     conversacion('Eligiste la opción 1')
# elif opcion == 2:
#     conversacion('Eligiste la opción 2')
# elif opcion == 3:
#     conversacion('Eligiste la opción 3')
# else:
#     print("error")


def suma(a,b):
    print("Sumando 2 numeros...")
    resultado = a + b
    return resultado

na= int(input("Ingresa número a "))
print(na)
nb= int(input("Ingresa número a "))
print(nb)

sumatoria = suma(na,nb)
print("Resultado suma = ", sumatoria)