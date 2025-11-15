# DUPLICA TODOS OS ELEMENTOS DE UMA LISTA

def imprime(lista):
    for item in lista:
        print(item*2)

lista_1 = [1, 2, 3, 4, 5]

print(imprime(lista_1))


# DUPLICA APENAS O PRIMEIRO ELEMENTO DA LISTA

def imprime(lista):
    print(lista[0]*2)
    for item in lista[1:]:
        print(item)
        

lista_2 = [1, 2, 3, 4, 5]

print(imprime(lista_2))


