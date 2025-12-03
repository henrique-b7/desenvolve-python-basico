#Exercício 2: Conversão de Temperatura
# Coletando a temperatura em Fahrenheit do usuário 
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
# Convertendo Fahrenheit para Celsius
celsius = (fahrenheit - 32) * 5.0/9.0
# Exibindo o resultado
print(f"{fahrenheit:.0f} graus Fahrenheit são {celsius:.0f} graus Celsius.")
# Fim do código 