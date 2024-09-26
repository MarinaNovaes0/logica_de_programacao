'''Desenvolva um sistema que receba o cadastro do nome de usuario e as 
#suas informações basicas, como, email e telefone, em seguida, calcule
#o gasto de combustivel mensal, considerando que o carro que ele usa tem
#capacidade total de 55 litros. Na gasolina ele tem autonomia de 14km/l, já
#no alcool a autonomia é de 12km/l. Considere que de casa ao trabalho são 32km
#e ele precisa ir e voltar do trabalho de segunda a sexta. 
#Qual será o gasto mensal (reais/litro) que o usuario terá no alcool e na gasolina? 
#Qual á média de kilometros rodados mensalmente'''

#informando nome, email e telefone
nome =input('\nDigite seu nome completo: ')
email =input('Digite o seu email: ')
fone =int(input ('Digite o seu telefone: '))

#informando km, valor da gasolina e valor do alcool 1ª semana
km1se= float(input('\nInforme quantos Km você percorreu na 1º semana: '))
gaso1 =float(input('Digite o valor do litro de gasolina na 1º semana : '))
alcool1 = float(input('Digite o valor do litro do álcool na 1º semana: '))
#variaveis de gasto 1º semana
gastogasos1 =gaso1*(km1se/14)
gastoalcos1 = alcool1*(km1se/12)

#informando km, valor da gasolina e valor do alcool 2ª semana
km2se= float(input('\nInforme quantos Km você percorreu na 2º semana: '))
gaso2 =float(input('Digite o valor do litro de gasolina na 2º semana : '))
alcool2= float(input('Digite o valor do litro do álcool na 2º semana: '))
#variaveis de gasto 2º semana
gastogasos2 =gaso2*(km2se/14)
gastoalcos2 = alcool2*(km2se/12)

#informando km, valor da gasolina e valor do alcool 3ª semana
km3se= float(input('\nInforme quantos Km você percorreu na 3º semana: '))
gaso3 =float(input('Digite o valor do litro de gasolina na 3º semana : '))
alcool3 = float(input('Digite o valor do litro do álcool na 3º semana: '))
#variaveis de gasto 3º semana
gastogasos3 =gaso3*(km3se/14)
gastoalcos3 = alcool3*(km3se/12)

#informando km, valor da gasolina e valor do alcool 4ª semana
km4se=float(input('\nInforme quantos Km você percorreu na 4º semana: '))
gaso4 =float(input('Digite o valor do litro de gasolina na 4º semana : '))
alcool4 = float(input('Digite o valor do litro do álcool na 4º semana: '))
#variaveis de gasto 4º semana
gastogasos4 =gaso4*(km4se/14)
gastoalcos4 = alcool4*(km4se/12)

#Variaveis soma final do preço da gasolina,do alcool e da distancia final
gastogasom= gastogasos1+gastogasos2+gastogasos3+gastogasos4
gastoalcoom= gastoalcos1+gastoalcos2+gastoalcos3+gastoalcos4
kmm= km1se+km2se+km3se+km4se

#Aparecendo as informaçoes
print(f'\nSeu nome é: {nome}')
print(f'Seu email é: {email}')
print(f'Seu telefone é: {fone}')
print(f'Você percorreu este mês {kmm}KM')
print(f'O gasto mensal se você abastecer com gasolina será: R${gastogasom:.2f}')
print(f'O gasto mensal se você abastecer com álcool será: R${gastoalcoom:.2f}')