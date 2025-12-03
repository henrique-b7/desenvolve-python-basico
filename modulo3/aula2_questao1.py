# Aula 2 Questão 1: Definindo se uma pessoa é maior de idade
# Coletando a idade de juliana e Cris
idade_ju = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))
# Definindo a maioridade
maioridade = idade_ju >= 18 and idade_cris >= 18
# Verificando se Juliana e Cris são maiores de idade
print(maioridade)