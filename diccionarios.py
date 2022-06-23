def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 45456765,
        'Mexico': 132547654,
        'Colombia': 51987572
    }

    #for pais in poblacion_paises.keys():
    #    print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' cuenta con ', poblacion, ' pobladores')


if __name__ == '__main__':
    run()