''' Jogo que escolhe um número aleatório entre 0 e 100 e o usuário
tenta acertar com 10 tentativas, entre as tentativas o sistema avisa 
se o número premiado é maior ou menor, no final se você ganhar ele
mostra os números tentados e o número de tetativas, quando você perde 
ele também mostra qual era o número premiado. '''

import random
import os

#Recebe um número aleatório entre 0 e 100
numero_premiado= random.randint(0,100)
num_tentados=[]
tentativas= 10

os.system('cls')
print (30*'*', 'Prepare-se!', 30*'*')
while True:
    print()
    print(f'Resta {tentativas} tentativas para acertar o número')
    ent_usuario= int(input("Digite um número: "))
    print()
    if ent_usuario == numero_premiado:
        os.system('cls')
        print (30*'*', 'Você ganhou!', 30*'*')
        break
    
    elif tentativas == 0:
        os.system('cls')
        print(30*'*', 'Você perdeu!', 30*'*')
        print(f'O número premiado era {numero_premiado}')
        break
    
    else:
        #Adiciona o número digitado na lista
        num_tentados.append(ent_usuario)
        tentativas -=1 
        
        #Verifica se o número digitado é maior ou menor
        if ent_usuario > numero_premiado:
            os.system('cls')
            print(30*'*', 'Errado!' ,30*'*')
            print()
            print("Digite um número menor!")
            print()
            print(69*'*')   
        else:
            os.system('cls')
            print(30*'*', 'Errado!' ,30*'*')
            print()
            print("Digite um número maior!")
            print()
            print(69*'*')
                      
print(f'Você tentou os números: {num_tentados}')
print(f'Você teve {len(num_tentados)} tentativas')
print(74*'*')
print("Fim do jogo!")
print()
print()