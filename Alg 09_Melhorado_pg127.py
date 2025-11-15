from collections import deque

grafo = {}
grafo["voce"] = ["Alice", "Bob", "Claire"]
grafo["Bob"] = ["Anuj", "Peggy"]
grafo["Alice"] = ["Peggy"]
grafo["Claire"] = ["Thom", "Jonny"]
grafo["Anuj"] = []
grafo["Peggy"] = []
grafo["Thom"] = []
grafo["Jonny"] = []

def pessoa_e_vendedor(nome):                                    #TESTA SE UMA PESSOA É VENDEDORA DE MANGAS.
    return nome[-1] == "y"                                      #CRITÉRIO UTILIZADO PARA SABER SE A PESSOA É VENDEDORA DE MANGAS.

def pesquisa(nome):
    fila_de_pesquisa = deque()                                  #CRIA UMA NOVA LISTA.    
    fila_de_pesquisa += grafo[nome]                             #ADICIONA OS VIZINHOS PARA A LISTA DE PESQUISA.
    verificadas = []                                            #VETOR QUE MANTÉM O REGISTRO DAS PESSOAS JÁ VERIFICADAS.
    vendedores = []                                             #VETOR QUE MANTÉM O REGISTRO DOS VENDEDORES JÁ IDENTIFICADOS.
    while fila_de_pesquisa:                                     #ENQUANTO A FILA NÃO ESTIVER VAZIA...
        pessoa = fila_de_pesquisa.popleft()                     #PEGUE A PRIMEIRA PESSOA DA FILA.
        if not pessoa in verificadas:                           #SE A PESSOA NÃO ESTIVER NA LISTA DE VERIFICADAS...
            if not pessoa in vendedores:                        #SE A PESSOA NÃO ESTIVER NA LISTA DE VENDEDORES JÁ IDENTIFICADOS...   
                if pessoa_e_vendedor(pessoa):                   #VERIFICA SE A PESSOA É VENDEDORA DE MANGA.
                    vendedores.append(pessoa)                   #ADICIONA A PESSOA VENDEDORA NA LISTA DE VENDEDORES.
                    print(pessoa + " é um vendedor de manga.")  #SIM, A PESSOA É VENDEDORA DE MANGA.
                    
                else:
                    fila_de_pesquisa += grafo[pessoa]           #NÃO, A PESSOA NÃO É VENDEDORA. ADICIONA TODOS OS AMIGOS DELA NA LISTA.
                    verificadas.append(pessoa)                  #ADICIONA A PESSOA NÃO VENDEDORA NA LISTA DE VERIFICADAS

    if not pessoa in vendedores:                                #NENHUMA PESSOA NA LISTA ERA VENDEDORA DE MANGAS.
        print("Não há vendedores de manga")


pesquisa("voce")
            