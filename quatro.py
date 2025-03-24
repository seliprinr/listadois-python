# Fazer um programa que leia 15 números de ponto flutuante armazenando-os em uma
# estrutura. Escreva a posição de cada número menor que zero dessa estrutura.

numeros = []

for i in range(15):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\nPosições dos números menores que zero:")
for i, num in enumerate(numeros):
    if num < 0:
        print(f"Número {num} na posição {i}")
