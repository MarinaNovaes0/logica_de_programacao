#Tipos de concatenação

#Concatenação com sinal +
nome = input('Digite seu nome: ')
print('Olá, '+ nome +'. Seja bem-vindo!')

# Não é possivel cacatenar numero inteiro usando este metodo,
# a menos que converta o numero inteiro em uma string

#Concatenação com a (,)
num = int(input('Digite um número inteiro: '))
num2=10
soma=num + num2
print('A soma é igual a:',soma)

#Concatenação com fstring (f)
print(f'O número digitado foi: {num}')
div = num /3
print(f'O resultado da divisão é: {div:.2f}')
# :.2f serve para definir quantas casas decimais irão aparecer
