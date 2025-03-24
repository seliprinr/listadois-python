# Faça um programa que leia um número indeterminado de notas de uma turma, a entrada de
# notas deve encerrar quando a nota informada for igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# a) Mostre a quantidade de valores que foram lidos;
# b) Exiba todos os valores na ordem em que foram digitados;
# c) Exiba todos os valores na ordem inversa;
# d) Calcule e mostre a soma dos valores;
# e) Calcule e mostre a média dos valores;
# f) Calcule e mostre a quantidade de valores acima da média calculada;
# g) Calcule e mostre a quantidade de valores abaixo de determinado valor de referência, que
# deve ser informado

notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

quantidade = len(notas)
print(f"\nQuantidade de valores lidos: {quantidade}")

print("Valores na ordem digitada:", notas)

print("Valores na ordem inversa:", list(reversed(notas)))

soma = sum(notas)
print(f"Soma dos valores: {soma}")

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0
print(f"Média dos valores: {media:.2f}")

acima_media = sum(1 for nota in notas if nota > media)
print(f"Quantidade de valores acima da média: {acima_media}")

referencia = float(input("\nInforme um valor de referência: "))
abaixo_referencia = sum(1 for nota in notas if nota < referencia)
print(f"Quantidade de valores abaixo de {referencia}: {abaixo_referencia}")
