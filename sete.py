# Ler uma palavra e duas letras, toda vez que a primeira letra aparecer substituí-la pela
# segunda. Apresentar a como resultado a nova palavra.

palavra = input("Digite uma palavra: ")
letra_antiga = input("Digite a letra que será substituída: ")
letra_nova = input("Digite a letra que irá substituir: ")

nova_palavra = palavra.replace(letra_antiga, letra_nova)

print(f"Nova palavra: {nova_palavra}")
