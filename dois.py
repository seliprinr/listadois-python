# Escreva um programa que lê duas notas de vários alunos e armazena esses dados em um
# dicionário, no qual o nome do aluno corresponde a chave. A entrada de dados deve terminar
# quando for informado um nome igual a “ ”. O programa deve receber o nome do aluno e
# retornar sua média correspondente.

alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou pressione Enter para encerrar): ").strip()
    if nome == "":
        break
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    media = (nota1 + nota2) / 2
    alunos[nome] = media

while True:
    busca = input("\nDigite o nome do aluno para consultar a média (ou pressione Enter para sair): ").strip()
    # A função .strip() em Python remove espaços em branco ou caracteres específicos do início e do final de uma string.
    # É uma função interna do Python.
    if busca == "":
        print("Encerrando o programa.")
        break
    if busca in alunos:
        print(f"A média de {busca} é {alunos[busca]:.2f}")
    else:
        print(f"Aluno '{busca}' não encontrado.")
