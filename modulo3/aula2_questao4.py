# Aula 2 questão 4: Valindando fichas dos personagens de um jogo RPG
# Definindo as variáveis de entrada
classe = input("Digite a classe do personagem (Guerreiro, Mago, Arqueiro): ")
forca = int(input("Digite o valor de Força (1-20): "))
magia = int(input("Digite o valor de Magia (1-20): "))
# Verificando a validade das fichas dos personagens
print ('Pontos de atributo consistentes com a classe escolhida:',(classe == "Guerreiro" and forca >= 15 and magia <= 10) or
       (classe == "Mago" and magia >= 15 and forca <= 10) or
       (classe == "Arqueiro" and forca >= 5 and magia >= 15))
# Fim do código