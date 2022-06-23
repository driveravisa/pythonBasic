from random import randint

def aleatorio(numero):
    num_aleatorio = randint(1,100)
    while numero != num_aleatorio:
        if numero < num_aleatorio:
            print("Ingresa un número más alto")
            numero = int(input("Nuevo número: "))
        else:
            print("ingresa un número más bajo")
            numero = int(input("Nuevo número: "))

    if numero == num_aleatorio:
        print("yes", num_aleatorio)
        return True


def run():
    menu = """
    |||  Adivina el número aleatorio del 1 al 100  ||| """
    print(menu)
    numero = int(input("Ingresa un número: "))
    if aleatorio(numero):
        print("Ganaste!, adivinaste el número")

if __name__ == '__main__':
    run()