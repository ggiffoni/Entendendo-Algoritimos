def imprime(lista):
    for item in lista:
        print(lista[0]*item)
    for item in lista:
        print(lista[1]*item)  
    for item in lista:
        print(lista[2]*item)
    for item in lista:
        print(lista[3]*item)
    for item in lista:
        print(lista[4]*item)              

lista_3 = [1, 2, 3, 4, 5]

print(imprime(lista_3))


import numpy as np

def multiplicar_array_por_cada_elemento(arr):
    """
    Multiplica cada elemento do array pelo array inteiro,
    gerando um novo array para cada elemento.
    
    Parâmetro:
    arr -- array NumPy (ou lista convertível para array)
    
    Retorna:
    lista de arrays, onde cada array é o original multiplicado por um de seus elementos
    """
    # Converte para array NumPy se ainda não for
    arr = np.array(arr)
    
    # Lista para armazenar os arrays resultantes
    arrays_multiplos = []
    
    # Para cada elemento no array original
    for elemento in arr:
        novo_array = arr * elemento  # Multiplicação elemento a elemento
        arrays_multiplos.append(novo_array)
    
    return arrays_multiplos

# Exemplo de uso
if __name__ == "__main__":
    # Array original
    original = [1, 2, 3, 4]
    
    # Gera os arrays múltiplos
    resultado = multiplicar_array_por_cada_elemento(original)
    
    # Exibe os resultados
    print(f"Array original: {original}")
    print("\nArrays gerados (multiplicação pelo próprio array):")
    for i, arr in enumerate(resultado):
        print(f"Multiplicado por {original[i]} -> {arr.tolist()}")