import numpy as np

def multiplicar_array_por_cada_elemento(arr):
    
    arr = np.array(arr)
    
    arrays_multiplos = []
    
    for elemento in arr:
        novo_array = arr * elemento  
        arrays_multiplos.append(novo_array)
    
    return arrays_multiplos

# Exemplo de uso

if __name__ == "__main__":
    
    original = [1, 2, 3, 4]
    
    resultado = multiplicar_array_por_cada_elemento(original)
    
    print(f"Array original: {original}")
    
    print("\nArrays gerados (multiplicação pelo próprio array):")
    
    for i, arr in enumerate(resultado):
        print(f"Multiplicado por {original[i]} -> {arr.tolist()}")