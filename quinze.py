# Faça um programa que leia uma matriz e encontre a linha que possui a menor soma. Se
# houver empate informe todos os valores das linhas que obtiveram a menor soma.

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
print("\nDigite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

somas = [sum(linha) for linha in matriz]
menor_soma = min(somas)

linhas_menor_soma = [i for i, soma in enumerate(somas) if soma == menor_soma]

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print(f"\nA menor soma encontrada foi: {menor_soma}")
print("Linha(s) com a menor soma:")
for linha_idx in linhas_menor_soma:
    print(f"Linha {linha_idx+1}: {matriz[linha_idx]}")

if len(linhas_menor_soma) > 1:
    print("\nHouve empate entre as linhas acima.")
