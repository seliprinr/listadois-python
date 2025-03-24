# Ler os dados de “N” pessoas (nome, sexo, idade e saúde), a leitura dos dados deve encerrar
# a entrada do nome informado for igual a “ ”. O programa deve apresentar como resultado o
# nome da pessoa e se ela está apta ou não para cumprir o serviço militar obrigatório no Brasil.
# Estão aptos ao serviço militar pessoas do sexo masculino, com 18 anos e sem problemas de
# saúde. O resultado também deve mostrar o número total de aptos ao serviço militar.

aptos = 0

while True:
    nome = input("Digite o nome da pessoa (ou pressione Enter para encerrar): ").strip()
    if nome == "":
        break
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    idade = int(input(f"Digite a idade de {nome}: "))
    saude = input(f"{nome} tem boa saúde? (S/N): ").strip().upper()

    if sexo == "M" and idade >= 18 and saude == "S":
        print(f"{nome} está apto para o serviço militar obrigatório.")
        aptos += 1
    else:
        print(f"{nome} NÃO está apto para o serviço militar obrigatório.")

print(f"\nNúmero total de pessoas aptas ao serviço militar: {aptos}")
