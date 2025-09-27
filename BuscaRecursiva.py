def busca_rec(lista, x):
    if len(lista) == 0:
        return False
    if lista[0] == x:
        return True
    return busca_rec(lista[1:], x)


lista_A = [3, 5, 7, 9]

print(busca_rec(lista_A, 5))


lista_B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_B[1:])
