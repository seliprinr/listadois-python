# Escrever um programa para ler uma matriz de ordem 5x5 de inteiros, contar e apresentar
# como resultado a quantidade de elementos ímpares, a quantidade de pares e quantos zeros
# existem na matriz.

matriz = []

pares = 0
impares = 0
zeros = 0

print("Digite os elementos da matriz 5x5:")
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(valor)

        if valor == 0:
            zeros += 1
        elif valor % 2 == 0:
            pares += 1
        else:
            impares += 1

    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de zeros: {zeros}")
