#Converção da temperatura de Fahrenheit para graus Celsius

Fahrenheit = input('Digite o valor da temperatura em Fahrenheint: ')
Fahrenheit = float(Fahrenheit)
celsius = (Fahrenheit-32)/1.8

print()
print(f"A temperatura convertida em celsius é: {celsius: .2f}")