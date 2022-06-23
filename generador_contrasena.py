import random

def password_generate():
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    mayusculas = ["A","B","C","D","E","F","G","H","I"]
    minusculas = ["a","b","c","d","e","f","g","h","i"]
    simbolos = ["/","*","%","@","#","$","?","!","&"]

    caracteres = numeros + mayusculas + minusculas + simbolos
    password = []

    for i in range(15):
        random_caracter = random.choice(caracteres)
        password.append(random_caracter)
    password = "".join(password)
    return password


def run():
    password = password_generate()
    print('Tu nueva contrasena es: ' + password)


if __name__ == '__main__':
    run()