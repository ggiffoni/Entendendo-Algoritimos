infinito = float("inf")

grafo = {}
grafo["A"] = {}
grafo["A"]["B"] = 5
grafo["A"]["C"] = 0
grafo["B"] = {}
grafo["B"]["D"] = 15
grafo["B"]["E"] = 10
grafo["C"] = {}
grafo["C"]["D"] = 20
grafo["C"]["E"] = 35
grafo["D"] = {}
grafo["D"]["F"] = 30
grafo["E"]= {}
grafo["E"]["F"] = 25
grafo["F"] = {}

custos = {}
custos["A"] = 0
custos["B"] = 5
custos["C"] = 0
custos["D"] = infinito
custos["E"] = infinito
custos["F"] = infinito

pais = {}
pais["A"] = None
pais["B"] = "A"
pais["C"] = "A"
pais["D"] = None
pais["E"] = None
pais["F"] = None

processados = []


def no_mais_barato(custos):
    custo_mais_barato = infinito
    no_mais_barato = None
    for no in custos:
        custo = custos[no]
        if custo < custo_mais_barato and no not in processados:
            custo_mais_barato = custo
            no_mais_barato = no

    return no_mais_barato    


destino = "F"
no = no_mais_barato(custos)
while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = no_mais_barato(custos)


print(grafo)
print(custos)
print(pais)    


def imprimir_caminho(pais, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pais.get(atual)
    if caminho[-1] == "A":
        caminho.reverse()
        return " -> ".join(caminho)
    else:
        return f"Nenhum caminho encontrado até o destino {destino}"
    

caminho = imprimir_caminho(pais, destino)

print("Melhor caminho até o nó", destino, ":", caminho)


          