# Aula 2 Questão 3: Verificar a qualificação para acesso ao clube de jogos de tabuleiro
# Definindo as variáveis de entrada
idade = int(input("Digite sua idade: "))
jogos = (input("Já jogou pelo menos 3 jogos de tabuleiro: "))
vitorias = int(input("Quantas jogos você já venceu? "))
# Verificando a qualificação para acesso ao Clube de Jogos de Tabuleiro
print (idade >= 16 or idade <= 18 and jogos == "sim" and vitorias >= 1)