# Aula 4 - Questão 1 
# Iniciando o cálculo do valor de um terreno coletando o comprimento do terreno
comp = float(input("Digite o comprimento do terreno em metros: "))
# Coletando a largura do terreno
largura = float(input("Digite a largura do terreno em metros: "))
# Coletando o valor do metro quadrado
valor_m2 = float(input("Digite o valor do metro quadrado do terreno em R$:"))
# Calculando a área do terreno
area = comp * largura
# Calculando o valor total do terreno
valor_total = area * valor_m2
# Exibindo o resultado final
print(f"O terreno possui {area} m² e custa R$ {valor_total:.2f}.")