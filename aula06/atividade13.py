print()
#Imprimindo a lista

nomes = ['Marina','Lucas','Rafael','Gomes','Fabiana','Daniel','Yasmin','João','Maria','Gabriel']
#Exibindo sem nenhuma alteração
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
nomes2 = ['Marina','Lucas','Rafael','Gomes','Fabiana','Daniel','Yasmin','João','Maria','Gabriel'] 

#Aparecendo apenas os 6 primeiros
del(nomes2[6:])
print(nomes2)
print()

#Restaurando a lista
nomes3 = ['Marina','Lucas','Rafael','Gomes','Fabiana','Daniel','Yasmin','João','Maria','Gabriel']

#Aparecendo apenas os 3 ultimos
del(nomes3[0:7])
print(nomes3)
print()