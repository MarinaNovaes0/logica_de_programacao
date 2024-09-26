'''
 Crie um programa que permita cadastrar 5 alunos. Para cada aluno, 
 armazene o nome e três notas. O programa deve calcular a média das notas 
 de cada aluno e armazenar as informações (nome e média) em um dicionário.
 Ao final,exiba o nome e a média de cada aluno
'''

import os
usuarios={}
while True:
    print()
    print()
    print (30*'*', 'Menu', 30*'*')
    print('1. Cadastrar Alunos e Notas')
    print('2. Listar Alunos e Médias')
    print('3. Sair')
    print(66*'*')
    print()
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        os.system('cls')
        nome = input("Digite o nome do aluno: ")
        n1= float(input('Digite a primeira nota: '))
        n2= float(input('Digite a segunda nota: '))
        n3= float(input('Digite a terceira nota: '))
        ntf=float((n1+n2+n3)/3)
        usuarios[nome]={'nome' : nome  , 'media' : ntf}     
        os.system('cls')   

    elif opcao == '2':
        os.system('cls')
        print (30*'*', 'Alunos', 30*'*')
        for nome, dados in usuarios.items():               
            print(f'Nome: {dados['nome']}, Média Final: {dados['media']}')
        print(68*'*')
            
    elif opcao =='3':
        print("Saindo do sistema")
        break
