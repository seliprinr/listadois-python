# Escreva um programa que leia uma palavra qualquer e verifique se esta palavra é um
# palíndromo.

palavra = input("Digite uma palavra: ")

palavra_limpa = palavra.replace(" ", "").lower()

if palavra_limpa == palavra_limpa[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
