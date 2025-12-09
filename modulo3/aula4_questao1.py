# Aula 4 Questão 1
# Informar se a soma de dois números é par ou ímpar
# Coletando os números do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
# Calculando a soma
soma = num1 + num2
# Verificando se a soma é par ou ímpar
if soma % 2 == 0:
    print(f"A soma de {num1} e {num2} é {soma}, que é um número par.")
else:
    print(f"A soma de {num1} e {num2} é {soma}, que é um número ímpar.")
# Fim do código.