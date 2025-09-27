def Maior(lista):
    if lista == []:
        return None
    else:
        maior = lista[0]
        for x in lista:
            if x > maior:
                maior = x
    return maior


lista_A = [14, 17, 32, 2, 4, 53, 8, 3]

print(Maior(lista_A))


def Menor(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return menor

lista_B = [77, 99, 38, 100, 500]


print(Menor(lista_B))


def Maior2(lista):
    if lista == []:
        return None
    else:
        maior = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > maior:
                maior = lista[i]
    return maior

lista_C = [12, 43, 456, 3, 7]

print(Maior2(lista_C))


def Menor2(lista):
    if lista == []:
        return None
    else:
        menor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] < menor:
                menor = lista[i]
    return menor

lista_D = [12, 43, 456, 3, 7, 0, 33, -18, 4]

print(Menor2(lista_D))

