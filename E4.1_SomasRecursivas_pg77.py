# SOMA "NORMAL" EM LOOP:
def soma_loop(arr):
    total = 0
    for x in arr:
        total += x
    return total


lista1 = [1, 4, 8, 10]

print(soma_loop(lista1))


# DO PRIMEIRO ELEMENTO DA LISTA PARA O ÚLTIMO:
def soma_recursiva(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + soma_recursiva(arr[1:])
    

lista2 = [1, 2, 3, 4, 5]    

print(soma_recursiva(lista2))


# DO ÚLTIMO ELEMENTO DA LISTA PARA O PRIMEIRO:
def soma_recursiva2(arr):
    qtd = len(arr)
    if qtd == 0:
        return 0
    ultimo = arr[qtd-1]
    sublista = arr[:-1]
    soma_sublista = soma_recursiva2(sublista)
    return ultimo + soma_sublista


lista3 = [2, 4, 7, 1]

print(soma_recursiva2(lista3))


# DO ÚLTIMO ELEMENTO DA LISTA PARA O PRIMEIRO:
def soma_recursiva(arr):
    if arr == []:
        return 0
    else:
        return arr[len(arr)-1] + soma_recursiva(arr[:-1])
    

lista4 = [1, 2, 3, 4, 5, 7]    

print(soma_recursiva(lista4))




