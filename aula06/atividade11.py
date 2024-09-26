#Criando a lista
lista = []
print("Vamos fazer uma lista com 10 números")
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
n4=int(input("Digite o quarto número: "))
n5=int(input("Digite o quinto número: "))
n6=int(input("Digite o sexto número: "))
n7=int(input("Digite o sétimo número: "))
n8=int(input("Digite o oitavo número: "))
n9=int(input("Digite o nono número: "))
n10=int(input("Digite o décimo número: "))

#append adiciona um valor
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)
lista.append(n5)
lista.append(n6)
lista.append(n7)
lista.append(n8)
lista.append(n9)
lista.append(n10)
print()
print("O resultado da lista: ")
print(lista)
print()

#Imprimindo o dobro da lista
print("O dobro da lista é: ")
print(f"[{n1*2}, {n2*2}, {n3*2}, {n4*2}, {n5*2}, {n6*2}, {n7*2}, {n8*2}, {n9*2}, {n10*2}]")