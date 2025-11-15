def Regressiva(i):
    print(i)
    if i <= 1:
        return 
    else:
        Regressiva(i-1)


a = Regressiva(8) 

print(a)

