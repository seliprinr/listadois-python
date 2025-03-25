# Fazer um programa que leia duas matrizes inteiras de ordem 4 e verifique se a soma dos
# elementos das diagonais principais são iguais.

def ler_matriz(nome):
    print(f"\nDigite os elementos da matriz {nome}:")
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(4):
        soma += matriz[i][i]
    return soma

matriz1 = ler_matriz("A")
matriz2 = ler_matriz("B")

soma_diag_1 = soma_diagonal_principal(matriz1)
soma_diag_2 = soma_diagonal_principal(matriz2)

print("\nMatriz A:")
for linha in matriz1:
    print(linha)

print("\nMatriz B:")
for linha in matriz2:
    print(linha)

print(f"\nSoma da diagonal principal da matriz A: {soma_diag_1}")
print(f"Soma da diagonal principal da matriz B: {soma_diag_2}")

if soma_diag_1 == soma_diag_2:
    print("\nAs somas das diagonais principais são iguais.")
else:
    print("\nAs somas das diagonais principais são diferentes.")
