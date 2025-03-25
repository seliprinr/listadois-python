# Faça um programa que leia números inteiros armazenando-os em uma matriz de 5 linhas por
# 5 colunas e a seguir escreva para cada linha o número desta e o seu maior elemento. Em
# seguida escreva para cada coluna o número desta e o seu menor elemento.

matriz = []

print("Digite os elementos da matriz 5x5:")
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print("\nMaior elemento de cada linha:")
for i in range(5):
    maior = max(matriz[i])
    print(f"Linha {i+1}: maior elemento = {maior}")

print("\nMenor elemento de cada coluna:")
for j in range(5):
    coluna = [matriz[i][j] for i in range(5)]
    menor = min(coluna)
    print(f"Coluna {j+1}: menor elemento = {menor}")
