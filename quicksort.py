def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [ i for i in lista[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))



def quicksort_2(arr):
    # Função principal que realiza o QuickSort
    if len(arr) <= 1:
        return arr  # Se o array tem 0 ou 1 elementos, já está ordenado.
    
    # Determina o pivô como o elemento central
    mid = len(arr) // 2
    pivot = arr[mid]
    
    # Divide o array em três partes: menores, iguais e maiores que o pivô
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Ordena recursivamente as partes e as combina
    return quicksort_2(left) + middle + quicksort_2(right)

print(quicksort_2([10, 5, 2, 3]))



def quicksort_3(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        pivo = lista[meio]
        
        menores = [i for i in lista if i < pivo]
        centro = [i for i in lista if i == pivo]
        maiores = [ i for i in lista if i > pivo]
        return quicksort_3(menores) + centro + quicksort_3(maiores)

print(quicksort_3([10, 5, 2, 3]))