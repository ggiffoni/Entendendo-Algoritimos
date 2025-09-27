def buscaMenor(arr):

# Considera inicialmente que o menor valor é o primeiro do array.    
    menor = arr[0]

# Considera inicialmente que o menor íncice é o zero.     
    menor_indice = 0

#Testa elemento por elemento buscando o menor valor e retorna o índice do menor valor.    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):

# Define um array vazio onde serão armazenados os menores valores.    
    novoArr = []

    for i in range(len(arr)):

# Define menor como o resultado da função buscaMenor que retorna o menor índice.         
        menor = buscaMenor(arr)

# Adiciona ao novo array o elemento do menor índice que, por sua vez, será o menor elemento. 
# O menor elemento também é retirado do array anterior.
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([5, 3, 6, 2, 10, 0, 23, 1]))
    