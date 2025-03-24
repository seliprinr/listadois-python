# Escrever um programa para ler uma string e copiar para dentro de uma outra string todas as
# vogais. Exibir na tela a string formada pelas letras copiadas.

texto = input("Digite uma string: ")

vogais = "aeiouAEIOU"
resultado = ""

for letra in texto:
    if letra in vogais:
        resultado += letra

print(f"String formada apenas pelas vogais: {resultado}")
