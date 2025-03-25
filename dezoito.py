# Faça um programa que leia um caractere e chame uma função para verificar se o caractere é
# uma vogal. Ao final, deve ser mostrada uma mensagem (dentro da main) indicando o
# resultado do teste. A função deve retornar 1 se for vogal e 0 caso contrário. Para simplificar,
# considere apenas as letras sem acentuação.

def verificar_vogal(caractere):
    if caractere.lower() in 'aeiou':
        return 1  # Vogal
    else:
        return 0  # Não é vogal

caractere = input("Digite um caractere: ")

resultado = verificar_vogal(caractere)

if resultado == 1:
    print(f"{caractere} é uma vogal.")
else:
    print(f"{caractere} não é uma vogal.")
