# Faça um programa que lê duas strings e chama uma função que retorna 1 se a menor está
# contida na maior, e 0 caso contrário. Por exemplo: a palavra ponta está contida em apontar.
# A menor palavra pode ser tanto a primeira quanto a segunda.

def verificar_conteudo(str1, str2):
    # Ordena as strings para garantir que sempre pegamos a menor e maior
    menor = min(str1, str2, key=len)
    maior = max(str1, str2, key=len)

    if menor in maior:
        return 1  # Menor string está contida na maior
    else:
        return 0  # Menor string não está contida na maior

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

resultado = verificar_conteudo(str1, str2)

if resultado == 1:
    print(f"A menor palavra está contida na maior.")
else:
    print(f"A menor palavra não está contida na maior.")
