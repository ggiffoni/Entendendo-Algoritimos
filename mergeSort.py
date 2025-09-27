def merge_sort(arr):
    if len(arr) > 1:
        # Dividindo o array em duas metades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Chamando recursivamente merge_sort nas duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        # Mesclando as duas metades
        i = j = k = 0

        # Comparando os elementos e combinando
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Adicionando os elementos restantes da metade esquerda, se houver
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Adicionando os elementos restantes da metade direita, se houver
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Exemplo de uso
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Array original:", array)
    merge_sort(array)
    print("Array ordenado:", array)
