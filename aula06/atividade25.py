valor_inicial= input('Digite o valor: ') #entrada de dados pelo cliente e conversão de valores
valor_inicial= float(valor_inicial)

taxa= input('Digite a taxa de juros: ')
taxa= float(taxa)

tempo= input('Digite o tempo que o dinheiro ficará: ')
tempo= float(tempo)

juros = valor_inicial*(taxa*tempo) #operação matemáticas

print(f'A estimativa de juros para o período indicado é: {juros:.2f}')