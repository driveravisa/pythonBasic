#Programa palindromo
def palindromo_func(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    es_palindromo = palabra[::-1]
    if es_palindromo == palabra:
        return True
    else:
        return False


def run():
    print("||| PROGRAMA PALINDROMO |||\n Bienvenido")
    palabra = input("Ingresa palabra o frase: ")
    palindromo = palindromo_func(palabra)

    if palindromo == True:
        print(palabra + " Es palindromo")
    else:
        print("No es palindromo")



if __name__ == '__main__':
    run()