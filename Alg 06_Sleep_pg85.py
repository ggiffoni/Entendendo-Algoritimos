def printlista(lista):
    for item in lista:
        print(item)

lista_1 = [1, 2, 3, 4, 5]

print(printlista(lista_1))


from time import sleep

def printlista_2(lista):
    for item in lista:
        sleep(1)
        print(item)

lista_2 = [1, 2, 3, 4, 5, 6, 7]

print(printlista_2(lista_2))


