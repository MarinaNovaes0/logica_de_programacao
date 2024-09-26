import os
usuarios={}

while True:
    
    print()
    print (30*'*', 'Menu', 30*'*')
    print('1. Cadastrar usuário')
    print('2. Listar usuário')
    print('3. Excluir usuário')
    print('4. Sair')
    print(66*'*')
    print()    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        nome = input("Digite o nome que deseja cadastrar: ").upper()
        cpf= input('Digite o cpf: ')
        email= input('Digite o email: ')
        usuarios[nome]={'nome' : nome  , 'cpf':  cpf, 'email' : email }     
        print('Usuário cadastrado com sucesso!')    
                 
    elif opcao == '2': 
        for email, dados in usuarios.items():    
            print(f'Nome: {dados['nome']}, Cpf: {dados['cpf']}, Email: {dados['email']}')
            
    elif opcao == '3':
        if not usuarios:
            print("Nenhum usuário cadastrado!")
        else:
            for dados in usuarios.values():  
                print(f'Nome: {dados["nome"]}, Cpf: {dados["cpf"]}, Email: {dados["email"]}')
            remover = input("Digite o nome que você deseja excluir: ").upper()
            if remover in usuarios: 
                del usuarios[remover]
                print(f'Usuário {remover} excluído com sucesso!')
            else:
                print("O nome não está na lista!")
            
    elif opcao =='4':
        print("Saindo do sistema")
        break        
