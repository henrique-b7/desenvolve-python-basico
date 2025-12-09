# Aula 4 Questão 2
# Definindo a nota de um filme com base na avaliação do público
# Coletando a nota atribuída pelo usuário
nota = int(input("Digite a nota do filme (1 a 5): "))
# Verificando a nota e exibindo a mensagem correspondente
if nota == 1:
    print("Ruim")
elif nota == 2:
    print("Regular")
elif nota == 3:
    print("Bom!")
elif nota == 4:
    print("Muito Bom!!")
elif nota == 5:
    print("Excelente!!!")
else:
    print("Nota inválida.")
# Fim do código