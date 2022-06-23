def run():
    contador = 0
    LIMITE = 10
    res=0
    while contador < LIMITE:
        num = 3
        res = num**contador
        res = round(res, 3)
        print (num, " elevado a ", contador , "= ", res)
        contador = contador + 1

if __name__ == '__main__':
    run()