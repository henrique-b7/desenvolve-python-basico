# Aula 2 Questão 5: Verificar aptidão para aposentadoria
#Início do Código
# Coletando o genero do usuário
genero = input("Digite seu gênero (M para masculino, F para feminino): ")
# Coletando o tempo de serviço do usuário
tempo_servico = int(input("Digite seu tempo de serviço em anos: "))
# Coletando a idade do usuário
idade = int(input("Digite sua idade em anos: "))
# Imprimndo as condições de aposentadoria
print("Você está apto para se aposentar:", 
      (genero == 'M' and tempo_servico >= 30 and idade >= 65) or 
      (genero == 'F' and tempo_servico >= 25 and idade >=60))
#Fim do Código