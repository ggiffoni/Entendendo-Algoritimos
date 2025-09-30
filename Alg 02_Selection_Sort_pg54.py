def buscaMenor(arr):

    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):

    novoArr = []

    for i in range(len(arr)):

        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([5, 3, 6, 2, 10, 0, 23, 1]))

# Array = [5, 3, 6, 2, 10, 0, 23, 1]

# Da função buscaMenor, temos: 
# menor = arr[5] = 0
# menor_indice = 5

# Da função ordenacaoporSelecao, temos na primeira iteração:
# menor = 0
# novoArr = [0]

# Segunda Iteração:
# Array = [5, 3, 6, 2, 10, 23, 1]
# menor = 1
# novoArr = [0, 1]

# Terceira Iteração:
# Array = [5, 3, 6, 2, 10, 23]
# menor = 2
# novoArr = [0, 1, 2]

    