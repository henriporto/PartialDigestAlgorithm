"""
Aluno: Henrique de Morais Porto
"""
from itertools import combinations

# 1) Escreva um algoritmo (ou programa em python) que, dado um conjunto X, calcula o multiset ΔX (e imprime).
def calcula_multiset(x):
    delta_x = []
    tamanho_x = len(x)
    for i in range(tamanho_x):
        for j in range(i+1, tamanho_x):
            delta_x.append(x[j] - x[i])
    return sorted(delta_x)


multiset = calcula_multiset([0, 3, 4, 5, 6, 9, 15])
print("Questão 1) Multiset encontrado:", multiset)


# 2) Considere a digestão parcial abaixo:
# L = {1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15} 
# Resolva o problema da digestão parcial para L (ou seja, ache X tal que ΔX = L).
def calcula_X(delta_x):
    delta_x = sorted(delta_x)
    maior_ponto = delta_x[-1]
    tamanho_delta_x = len(delta_x)
    tamanho_x = int((1+(1+(8*tamanho_delta_x))**0.5)/2) # Bhaskara

    for subconjunto in combinations(range(1, maior_ponto), tamanho_x - 2):
        X = [0] + list(subconjunto) + [maior_ponto]
        X = sorted(X)
        if calcula_multiset(X) == delta_x:
            return X


L = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
X = calcula_X(L)
print("Questão 2) Conjunto X encontrado:", X)