# Escrever um programa para ler uma string e um número n, e eliminar n caracteres do final da
# string. A string resultante deve ser mostrada na tela. Por exemplo, lida a string Agora e o
# número 3, deve mostrar na tela a palavra Ag.

texto = input("Digite uma string: ")
n = int(input("Digite a quantidade de caracteres a serem removidos do final: "))

resultado = texto[:-n] if n <= len(texto) else ""

print(f"String resultante: {resultado}")
