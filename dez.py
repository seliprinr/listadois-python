# Ler uma palavra e uma letra qualquer. Mostrar a palavra cortada na primeira posição em que
# encontrar a letra informada.

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

posicao = palavra.find(letra)

if posicao != -1:
    print("Palavra cortada:", palavra[:posicao])
else:
    print("Letra não encontrada na palavra.")
