#Criando uma lista
nomes = []
print("Vamos fazer uma lista com 10 nomes")
n1=input("Digite o primeiro: ")
n2=input("Digite o segundo: ")
n3=input("Digite o terceiro: ")
n4=input("Digite o quarto: ")
n5=input("Digite o quinto: ")
n6=input("Digite o sexto: ")
n7=input("Digite o sétimo: ")
n8=input("Digite o oitavo: ")
n9=input("Digite o nono: ")
n10=input("Digite o décimo: ")

#append adiciona um valor
nomes.append(n1)
nomes.append(n2)
nomes.append(n3)
nomes.append(n4)
nomes.append(n5)
nomes.append(n6)
nomes.append(n7)
nomes.append(n8)
nomes.append(n9)
nomes.append(n10)

#Imprimindo a lista
print(nomes)
print()

#Exibindo apenas o primeiro nome
print(nomes[0])
print()

#Exibindo apenas o quinto nome
print(nomes[4])
print()

#Deixando apenas os 2º e 3º nomes
del(nomes[0])
del(nomes[2:])
print(nomes)
print()

#Restaurando a lista
nomes2=[]
nomes2.append(n1)
nomes2.append(n2)
nomes2.append(n3)
nomes2.append(n4)
nomes2.append(n5)
nomes2.append(n6)
nomes2.append(n7)
nomes2.append(n8)
nomes2.append(n9)
nomes2.append(n10)


#Aparecendo apenas os 6 primeiros
del(nomes2[6:])
print(nomes2)
print()

#Restaurando a lista
nomes3 = []
nomes3.append(n1)
nomes3.append(n2)
nomes3.append(n3)
nomes3.append(n4)
nomes3.append(n5)
nomes3.append(n6)
nomes3.append(n7)
nomes3.append(n8)
nomes3.append(n9)
nomes3.append(n10)

#Aparecendo apenas os 3 ultimos
del(nomes3[0:7])
print(nomes3)
print()