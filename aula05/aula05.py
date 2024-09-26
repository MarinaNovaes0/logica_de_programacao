
lista1 = [1,2,3,4,5,6,7,8,9,10]

print(lista1[0])
# os : representa a partir de
print(lista1[2:])

#indices negativos sao tratados de maneira especial, 
#o -1 é considerado o último elemento
print(lista1[-1])

lista_int = [10,5,6,9,24,56,72,13,22,8]
print(lista_int)

#Ordem crescente
lista_int .sort()
print(lista_int)

#Ordem decrescente
lista_int .sort(reverse=True)
print(lista_int)

print(f'Lista ordenada direto no print: {sorted(lista_int, reverse=True)}')
#.remove remove da lista informando o valor, não índice
lista_int.remove(5)
print(lista_int)

#.pop Remove da lista informando o índice(posição que ocupa)
#funciona também com índices negativos
lista_int.pop(1)
print(lista_int)

#Também funciona para nomes
nomes = ['Marina','Lucas','Rafael','Gomes','Fabiana']

nomes.remove('Marina')
print(nomes)

nomes.pop(2)
print(nomes)

#inserindo itens na lista
lista_nomes = []
novo_nome=input("Digite um novo nome: ")

#append adiciona um valor
lista_nomes.append(novo_nome)
print(lista_nomes)
