import os
lista_prod= []
lista_quant=[]
lista_preco=[]

while True:
    
    print()
    print (30*'*', 'Menu', 30*'*')
    print('1. Adicionar produtos')
    print('2. Atualizar quantidade de produtos')
    print('3. Listar produtos')
    print('4. Valor total do estoque')
    print('5. Sair')
    print(66*'*')
    print()
    
    opcao = input("Digite a opção desejada: ")
    
    # Adicionar produtos
    if opcao == '1':
        prod = input("Digite o nome do produto: ")
        quant = int(input("Digite a quantidade produto: "))
        preco = float(input("Digite o valor do produto: "))
        
        if prod != '':
            lista_prod.append(prod)
            lista_quant.append(quant)
            lista_preco.append(preco)  
            print(f"{prod} cadastrado com sucesso!")

        else:
            print("Verifique os dados digitados!")
            
    #Atualizar a quantidade
    elif opcao == '2':
            os.system('cls')
            print(66*'*')
            for i, (produto, quantidade) in enumerate(zip(lista_prod, lista_quant), start=1):              
                print(f'Produto {i}: {produto} - Quantidade: {quantidade}')
            print(66*'*')
            print() 
                         
            posicao = int(input("Digite o número do produto que deseja mudar a quantidade: "))
           
            if 1 <= posicao <= len(lista_prod):
                nova_quant= int(input('Digite a nova quantidade: '))
                lista_quant[posicao - 1] = nova_quant
                os.system('cls')
                print(24* '*', "Lista Atualizada", 24* '*')
                for i, (produto, quantidade) in enumerate(zip(lista_prod, lista_quant), start=1):              
                    print(f'Produto {i}: {produto} - Quantidade: {quantidade}')
                print(66*'*')
                print()
                   
            else:
                print("Escolha uma opção válida")
            
    #Listar produtos
    elif opcao == '3':
           if not lista_prod:
            print("Não há produtos cadastrados")
           
           else:
            os.system('cls')
            print(66*'*')
            for i, (produto, quantidade, preco) in enumerate(zip(lista_prod, lista_quant, lista_preco), start=1):
                print(f'Produto {i}: {produto} - Quantidade: {quantidade} - Preço: R${preco:.2f}')
            print(66*'*') 
            print()
                             
    #Soma produtos
    elif opcao == '4':
            if lista_preco:
                total_precos = sum(lista_preco)
                print(f"O valor total do estoque é: R${total_precos:.2f}")
            else:
                print("Não há produtos cadastrados para calcular o valor total.")
    
    #Sair
    elif opcao== '5':
        print('Saindo do sistema')
        break
    else:
        print("Digite uma opção válida!")