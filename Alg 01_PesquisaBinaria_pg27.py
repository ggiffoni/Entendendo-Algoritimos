def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2

# O chute é o elemento central da lista:        
        chute = lista[meio]

# Se o chute é igual ao item, o retorno é a posição do item:        
        if chute == item:
            return meio

# Se o chute (elemento central da lista) for maior que o item procurado, isso significa que devemos procurar o item na primeira metade
# da lista descartando o elemento central já testado. Isso é conseguido fazendo "alto = meio - 1":         
        if chute > item:
            alto = meio - 1

# Se o chute (elemento central da lista) for menor que o item procurado, isso significa que devemos procurar o item na segunda metade
# da lista descartando o elemento central já testado. Isso é conseguido fazendo "baixo = meio + 1": 
        else:
            baixo = meio + 1

# Se nada for encontrado, o retorno é None:            

    return None

minha_lista = [1, 3, 5, 7, 9, 11, 13, 14, 18] 

a = pesquisa_binaria(minha_lista, 11)
b = pesquisa_binaria(minha_lista, 3)

print(a)
print(b)

