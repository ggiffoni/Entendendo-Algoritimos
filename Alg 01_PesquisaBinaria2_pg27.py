def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista = list(range(1, 129)) 

minha_lista2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

a = pesquisa_binaria(minha_lista, 88)
b = pesquisa_binaria(minha_lista, -1)
c = pesquisa_binaria(minha_lista2, 30)

print(a)
print(b)
print(c)






