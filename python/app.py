# #!/usr/bin/env python
# from itertools import chain


# def seed(lines=1, columns=1, position=1, array=[], automatic=True):
#     """Funcao responsavel por gerar os arrays dinamicos ou passados"""
#     if position <= lines:
#         if len(array) > 0 and position == 1:
#             itens = [i for i in array]
#             automatic = False
#             array.clear()
#         elif automatic:
#             itens = [i for i in range(1, columns)]
#         else:
#             itens = [i for i in array[0][:-1]]
#         itens.append(sum(itens))
#         array.append(itens)
#         seed(lines, columns, position + 1, array, automatic)
#     return array


# def shuffle(array, n=1):
#     return [i[-n:] + i[:-n] for i in array]


# def escadinha(array, n=1):
#     counter = 0
#     result = []
#     for index, item in enumerate(array, start=n):
#         if counter == len(array[:-1]):
#             result.append(shuffle([item], 1))
#         else:
#             result.append(shuffle([item], index))
#         counter += 1
#     return list(chain(*result))


# if __name__ == "__main__":
#     matriz_correta = seed(lines=12, columns=13)
#     matriz_escadinha = escadinha(matriz_correta, 3)

#     print(matriz_correta)
#     print('\n')
#     print(matriz_escadinha)


# Resolver problema Escadinha 
matrizCorreta = [
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
]

matrizEscadinha = [
[11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8],
[8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7],
[7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
[4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2],
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
]

matrizEscadinhaEstendida = [
[11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8],
[8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7],
[7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
[4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2],
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
[11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8],
[8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7],
[7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
]

matrizEscadinhaReversa = [
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
[6, 7, 8, 9, 10, 11, 12, 78,1, 2, 3, 4, 5],
[7, 8, 9, 10, 11, 12, 78,1, 2, 3, 4, 5, 6],
[8, 9, 10, 11, 12, 78,1, 2, 3, 4, 5, 6, 7],
[9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
[78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2]
]

matrizInutilizavel_1 =[
[11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8],
[8, 9, 10, 11, 12, 2, 1, 78, 3, 4, 5, 6, 7],
[7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
[4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2],
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
]

matrizInutilizavel_2 =[
[11, 12, 1, 2, 78, 3, 4, 5, 6, 7, 8, 9, 10],
[10, 11, 12, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 78],
[8, 9, 10, 11, 12, 2, 1, 78, 3, 4, 5, 6, 7],
[7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3, 4],
[4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2, 3],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1, 2],
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 1],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
]

matrizNegativaEscadinha =[
[0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]
]

matrizNegativaCorreta =[
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0],
]

matrizNegativaConflito =[
[0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0],
[0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0],
[0, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]
]

matrizNegativaInvalida =[
[-1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1, -1],
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 1],
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0],
[0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0],
[0, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]
]

#
# Funcao que detecta padrao 'escadinha'
# Entrada: matriz com valores dos meses e coluna total (em qualquer posicao)
# Saidas: lValida = indicacao de padrao valido (escadinha ou matriz correta)
#         k = lista com quantidades de deslocamentos 
# obs: k precisa ser uma lista porque se forem admitidos valores negativos
#      podem ocorrer situacoes com soma 0 validas (ex: matrizNegativaConflito)
#
def detectaEscadinha(matrizIn): 
    
    nLinhas = len(matrizIn)
    nCols = len(matrizIn[0])

    matrizN = [0] * nCols
    
    nUltimaCol = 0
    for n,linha in enumerate(matrizIn):
        somaLinha = sum(linha)

        nAjust = n%(nCols)

        for i,val in enumerate(linha):
            if (somaLinha - val) == val:
                if i == (nCols - 1):
                    nUltimaCol += 1
                
                matrizN[(i + 1 - nAjust)%nCols] += 1

    lValida = False
    
    k = []
    
    for i,val in enumerate(matrizN):
        if val == nLinhas:
            k.append(i)
            lValida = True

    if nUltimaCol == nLinhas:
        lValida = True
        k.append(0)

    return lValida, k    

#
# Funcao que ajusta matriz no padrao 'escadinha'
# Entrada: matriz com valores dos meses e coluna total (em qualquer posicao)
#          k = deslocamento
# Saidas: matriz corrigida
#
def corrigeEscadinha(matrizIn, k):
    nCols = len(matrizIn[0])
        
    matrizRet = []
    
    for n,linha in enumerate(matrizIn):

        nAjust = n%(nCols)
        
        matrizAux = [0] * nCols

        for i,val in enumerate(linha):
            x = (i - (nAjust + k))
            if x < 0:
                x = nCols + x

            matrizAux[x] = val
        
        matrizRet.append(matrizAux)
    
    return matrizRet

#
#Funcao de Impressao de resultados para validacao
#
def printResult(matrizIn):
    lValida, k = detectaEscadinha(matrizIn)

    if lValida:
        if len(k) == 1 and k[0] == 0:
            print("=> Matriz correta.")
            
        else:
            for val in k:
                print("=> Padrao escadinha detectado. k=", val)
                print(corrigeEscadinha(matrizIn, val))

    else:
        print("=> Matriz inutilizavel.")

#########################################################################
# Execucao dos cenarios
print("\nmatrizCorreta", )
printResult(matrizCorreta)

print("\nmatrizEscadinha")
printResult(matrizEscadinha)

print("\nmatrizEscadinhaEstendida")
printResult(matrizEscadinhaEstendida)

print("\nmatrizEscadinhaReversa")
printResult(matrizEscadinhaReversa)

print("\nmatrizInutilizavel_1")
printResult(matrizInutilizavel_1)

print("\nmatrizInutilizavel_2")
printResult(matrizInutilizavel_2)

print("\nmatrizNegativaEscadinha")
printResult(matrizNegativaEscadinha)

print("\nmatrizNegativaCorreta")
printResult(matrizNegativaCorreta)

print("\nmatrizNegativaConflito")
printResult(matrizNegativaConflito)

print("\nmatrizNegativaInvalida")
printResult(matrizNegativaInvalida)