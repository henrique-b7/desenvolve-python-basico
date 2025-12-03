# Aula 4 - Questão 4
# Programa para calcular a quantidade mínima de notas necessárias para compor um valor em reais.
# Coletando os dados de entrada
valor = int(input("Digite o valor em reais: "))
# Inicializando a contagem de notas e calculando a quantidade de cada nota
# Dividindo o valor pelas notas disponíveis e atualizando o valor restante
n100 = valor // 100
valor = valor % 100
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n50 = valor // 50
valor = valor % 50
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n20 = valor // 20
valor = valor % 20
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n10 = valor // 10
valor = valor % 10
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n5 = valor // 5
valor = valor % 5
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n2 = valor // 2
valor = valor % 2
# dividindo o valor pelas notas disponíveis e atualizando o valor restante
n1 = valor
# Exibindo o resultado
print(f"{n100} nota(s) de R$100,00")
print(f"{n50} nota(s) de R$50,00")
print(f"{n20} nota(s) de R$20,00")
print(f"{n10} nota(s) de R$10,00")
print(f"{n5} nota(s) de R$5,00")
print(f"{n2} nota(s) de R$2,00")
print(f"{n1} nota(s) de R$1,00")
# Fim do código