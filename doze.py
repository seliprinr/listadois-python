# Faça um programa que leia uma matriz 10x10 de elementos reais. O programa deve
# apresentar o menor valor e o maior valor, cada qual com sua respectiva posição (linha,
# coluna) na matriz.

matriz = []

menor_valor = float('inf')
maior_valor = float('-inf')
pos_menor = (0, 0)
pos_maior = (0, 0)

print("Digite os elementos da matriz 10x10:")
for i in range(10):
    linha = []
    for j in range(10):
        valor = float(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(valor)

        if valor < menor_valor:
            menor_valor = valor
            pos_menor = (i, j)
        if valor > maior_valor:
            maior_valor = valor
            pos_maior = (i, j)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print(f"\nMenor valor: {menor_valor} na posição (linha {pos_menor[0]+1}, coluna {pos_menor[1]+1})")
print(f"Maior valor: {maior_valor} na posição (linha {pos_maior[0]+1}, coluna {pos_maior[1]+1})")
