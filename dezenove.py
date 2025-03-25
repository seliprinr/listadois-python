# Faça um programa que leia uma string chame uma função para calcular o número de vogais
# desta. Se a string for vazia, exibir uma mensagem de alerta. A função que conta as vogais
# deve testar se cada letra é vogal utilizando a função do exercício anterior.

def verificar_vogal(caractere):
    if caractere.lower() in 'aeiou':
        return 1  # Vogal
    else:
        return 0  # Não é vogal


def contar_vogais(string):
    contador = 0
    for caractere in string:
        if verificar_vogal(caractere):
            contador += 1
    return contador


string = input("Digite uma string: ")

if not string:
    print("A string está vazia! Por favor, digite uma string.")
else:
    numero_vogais = contar_vogais(string)

    print(f"A string '{string}' tem {numero_vogais} vogais.")
