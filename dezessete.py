# Escrever um programa com uma função que retorna a soma dos números inteiros que
# existem entre n1 e n2 (inclusive ambos). A função deve funcionar inclusive se o valor de n2
# for menor que n1. Ler n1 e n2 no programa principal.

def soma_inteiros_entre(n1, n2):
    inicio = min(n1, n2)
    fim = max(n1, n2)
    return sum(range(inicio, fim + 1))

n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))

resultado = soma_inteiros_entre(n1, n2)

print(f"A soma dos números inteiros entre {n1} e {n2} (inclusive) é: {resultado}")
