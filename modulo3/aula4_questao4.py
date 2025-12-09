# Aula 4 questão 4
# Cálculo do valor de frete
# Coletando os dados de entrada
peso = float(input("Digite o peso da encomenda em kg: "))
distancia = float(input("Digite a distância em km: "))
# Definindo os valores das tarifas
d100 = 1  # tarifa para até 100 km
d300 = 1.5  # tarifa para 101 a 300 km
dacima = 2  # tarifa para acima de 300 km
taxa_peso = 10  # taxa adicional para pacotes acima de 10 kg
# Calculando o valor do frete
if distancia <= 100:
    tarifa = d100
elif distancia <= 300:
    tarifa = d300
else:
    tarifa = dacima
frete = tarifa * distancia
if peso > 10:
    frete += taxa_peso
# Exibindo o valor do frete
print(f"O valor do frete é: R$ {frete:.2f}")
# Fim do programa