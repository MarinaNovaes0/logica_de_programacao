import os
lista_usuarios= []

while True:
    
    print()
    print (30*'*', 'Menu', 30*'*')
    print('1. Cadastrar usuário')
    print('2. Listar usuário')
    print('3. Excluir usuário')
    print('4. Buscar pelo nome')
    print('5. Inserir em uma posição')
    print('6. Sair')
    print(66*'*')
    print()
    
    opcao = input("Digite a opção desejada: ")
    
    # Cadastrar usuario
    if opcao == '1':
        nome = input("Digite o nome que deseja cadastrar: ").upper()
        
        if nome != '':
            lista_usuarios.append(nome)
            print(f"Usuário {nome} cadstrado com sucesso!")
        else:
            print("Digite algum valor!")
            
    #Listar usuarios
    elif opcao == '2':
        for i,n in enumerate(lista_usuarios):
            print(f'{i + 1}º {n}')
            
    #Excluir
    elif opcao == '3':    
        for i,n in enumerate(lista_usuarios):
            print(f'{i}: {n}')
        
        posicao = int(input("Digite o número do usuário que deseja excluir: "))
        for j, _ in enumerate(lista_usuarios):
                if j == posicao:
                    lista_usuarios.pop(j)
                    print(f'Usuário de posição {j} foi removido')    
     
   #Buscar pelo nome
    elif opcao == '4':
        nome_buscar= input("Digite o nome do usuário que deseja buscar: ").upper()
        
        if nome_buscar != '':
            for i in lista_usuarios:
                if i == nome_buscar:
                    print(i)
        else:
            print('Digite um nome')
                    
    #Inserir em uma posição
    elif opcao == '5':
        novo_nome= input('Digite o nome que deseja inserir: ').upper()
        posicao_nome= int(input('Digite a posição que deseja inserir: '))
        
        #Correção da posição
        posicao_nome -=1
        if posicao_nome >= 0 and posicao_nome <= len(lista_usuarios):
            lista_usuarios.insert(posicao_nome, novo_nome)
            for i,n in enumerate(lista_usuarios):
                print(f'{i + 1}º {n}')
            
        else:
            print('Posição inválida')
            
    #Sair
    elif opcao == '6':
        print('Saindo do sistema')
        break
    else:
        print("Digite uma opção válida!")