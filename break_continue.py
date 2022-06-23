def run():
    # for contador in range (100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(100):
    #     print(i)
    #     if i == 53:
    #         break
    
    palabra = input("Ingresa una palabra para deletrear, con excepción de la letra R: ")
    for i in palabra:
        if i == 'r' or i == 'R':
            print("Error letra 'R' detectada")
            break
        print(i)

if __name__ == '__main__':
    run()