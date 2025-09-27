def recursiva(i):
    if i < 1:
        return
    else:
        print(i)
        recursiva(i - 1)


a = recursiva(10)

print(a)


def recursiva2(r):
    print(r)
    if r < 1:
        return
    else:
        recursiva2(r - 1)


b = recursiva2(10)

print(b)
    
        




