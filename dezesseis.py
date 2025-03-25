# Na teoria dos Sistemas, define-se como elemento minimax de uma matriz, o menor elemento
# da linha em que se encontra o maior elemento da matriz. Escreva um programa que lê uma
# matriz [10 X 10] e em uma função encontre e mostre o elemento minimax e sua posição na
# matriz.

def encontrar_minimax(matriz):
    maior_elemento = float('-inf')
    pos_maior = (0, 0)

    for i in range(10):
        for j in range(10):
            if matriz[i][j] > maior_elemento:
                maior_elemento = matriz[i][j]
                pos_maior = (i, j)

    linha_maior = matriz[pos_maior[0]]
    minimax = min(linha_maior)
    coluna_minimax = linha_maior.index(minimax)

    return minimax, pos_maior[0], coluna_minimax

matriz = []
print("Digite os elementos da matriz 10x10:")
for i in range(10):
    linha = []
    for j in range(10):
        valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

minimax, linha, coluna = encontrar_minimax(matriz)

print("\nMatriz digitada:")
for linha_matriz in matriz:
    print(linha_matriz)

print(f"\nO elemento minimax é {minimax}, encontrado na linha {linha+1} e coluna {coluna+1}.")
