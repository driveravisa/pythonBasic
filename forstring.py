def run():
    cadena = input("Ingresa una palabra: ")
    for i in cadena[::1]:
        print(i.upper())

if __name__ == '__main__':
    run()