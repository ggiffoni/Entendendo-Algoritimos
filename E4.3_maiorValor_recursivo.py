def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max


lista_A = [2, 5, 4, 1, 3]

print(maximo(lista_A))


def maximo2a(lista):
    qtd = len(lista)
    if qtd == 1:
        return 0
    iatual = qtd - 1
    imaior_sublista = maximo2a(lista[:-1])
    if lista[iatual] > lista[imaior_sublista]:
        imaior = iatual
    else:
        imaior = imaior_sublista
    return imaior


def maximo2b(lista):
    res = maximo2a(lista)
    return lista[res]


lista_B = [2, 3, 4, 1, 5, 10, 0]

print(maximo2b(lista_B))


def maximo3(lista):
    if len(lista) == 0:
        return 0
    subMax = maximo3(lista[1:])
    if lista[0] < subMax:
        return subMax
    else:
        return lista[0]
    

lista_C = [2, 3, 4, 44, 1, 5, 10, 0]

print(maximo3(lista_C))


def maximo4(lista):
    if len(lista) == 0:
        return 0
    subMax = maximo4(lista[1:])
    if lista[0] < subMax:
        return subMax
    else:
        return lista[0]
  
    

lista_D = [2, 3, 4, 44, 1, 5, 94, 10, 0, 23]

print(maximo4(lista_D))


def maximo5(lista):
    if len(lista) == 0:
        return 0
    else:
        subMax = maximo5(lista[1:])
        if lista[0] < subMax:
            return subMax
        else:
            return lista[0]
  
    

lista_E = [94, 3, 4, 44, 1, 5, 2, 98, 10, 0, 23]

print(maximo5(lista_E))


def maximo6(lista):
    if len(lista) == 1:
        return lista[len(lista) - 1]
    subMax = maximo6(lista[1:])
    if lista[0] < subMax:
        return subMax
    else:
        return lista[0]

lista_F = [1, 2, 3, 4, 99, 2, 85, 100, 13, 22, 0]

print(maximo6(lista_F))


def maximo7(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    subMax = maximo7(lista[1:])
    if lista[0] < subMax:
        return subMax
    else:
        return lista[0]

lista_G = [1, 2, 3, 4, 99, 104, 2, 85, 100, 13, 22, 0, 32]

print(maximo7(lista_G))






  


