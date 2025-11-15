def maximo(lista):
    if len(lista) == 0:
        return 0
    else:
        subMax = maximo(lista[1:])
        if lista[0] < subMax:
            return subMax
        else:
            return lista[0]
        
lista_A = [94, 3, 4, 44, 1, 5, 2, 89, 10, 0, 23]

print(maximo(lista_A))


def maxima1(lista):
    if len(lista) == 0:
        return 0
    else:
        return maxima2(lista, lista[0])
    
def maxima2(lista, max):
    if len(lista) == 0:
        return max
    if lista[0] > max:
        max = lista[0]

    return maxima2(lista[1:], max)

lista_B = [3, 5, 7, 17, 4, 11, 2]

print(maxima1(lista_B))



def maximoTeste(lista):
    if len(lista) == 0:
        return 0
    else:
        subMax = maximoTeste(lista[1:])
        return subMax
        
lista_C = [32, 94, 3, 4, 44, 1, 5, 2, 89, 10, 23]

print(maximoTeste(lista_C))


def Max(list):
    if len(list) <= 1:
        return 0
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
    

lista_D = [32, 94, 3, 4, 44, 1, 5, 2, 89, 10, 23]

print(Max(lista_D))


def maximum(A):
    """
    find the maximum element of a list A recursively
    """
    # check if the list is short enough to do explicitly
    if len(A) < 4:
        return max(A)

    # else, we will use recursion to solve the problem
    n = len(A) // 2 # partition the list into two halves here
    max1 = maximum(A[:n]) # left half
    max2 = maximum(A[n:]) # right half
    
    return max(max1, max2)
    
A = list(range(100))
print(maximum(A))

# To write a recursive function in Python for finding the minimum and maximum values in a sequence without using any loops, 
# you'll need to evaluate the first item in the list against the remaining list in each recursion step. For reversing a list 
# using recursion, you need to extract and append the last element of the list to your result in each recursion step. Here are the sample codes:

def find_min_max(L):
    if len(L) == 1:
        return L[0], L[0]
    else:
        min_val, max_val = find_min_max(L[1:])
    return min(min_val, L[0]), max(max_val, L[0])

lista_E = [45, 64, 33, 2, 14, 77, 22, 13]

print(find_min_max(lista_E))


def reverse_list(L):
    if len(L) == 0:
        return []
    else:
        return reverse_list(L[1:]) + [L[0]]
    

def find_min(my_list):
  if len(my_list) == 0:
    return None
  if len(my_list) == 1:
    return my_list[0]
  #compare the first 2 elements
  temp = my_list[0] if my_list[0] < my_list[1] else my_list[1]
  my_list[1] = temp
  return find_min(my_list[1:])

print(find_min([]))
print(find_min([42, 17, 2, -1, 67]))    