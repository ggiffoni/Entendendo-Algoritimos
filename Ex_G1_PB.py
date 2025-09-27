def PB(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio -1

        if chute < item:
            baixo = meio + 1

        
    return None

List_A = [2, 4, 6, 8, 10, 22, 56] 

C = PB(List_A, 22)

print(C)

    