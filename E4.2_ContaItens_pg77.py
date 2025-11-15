def conta(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta(lista[1:])
    

lista = ["a", "b", "c", "d", "e", "f"]

print(conta(lista))