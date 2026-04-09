#SISTEMA DE OUVIDORIA DE RECLAMAÇÕES DE UMA EMPRESA FICCTÍCIA
#MEMBROS DO GRUPO: JOÃO PEDRO FLORÊNCIO, ÍTALO FELIPE, RAFAEL ABÍLIO, JULIAN, SAMUEL NUNES

reclamacoes=[]
sistema=True


def listar_reclamacoes():
     print('Lista de reclamações:')

     if len(reclamacoes)==0:
            print('Nenhuma reclamação cadastrada')

     else:
             for i, rec in enumerate(reclamacoes, start=1):
                 print(i,'-',rec)


while sistema:

    print(' ')
    print(' ')
    print('=========SISTEMA DE OUVIDORIA=========')
    print('1)Listar reclamações')
    print('--------------------------------------')
    print('2)Registrar nova reclamação')
    print('--------------------------------------')
    print('3)Pesquisar reclamação pelo código')
    print('--------------------------------------')
    print('4)Atualizar reclamação')
    print('--------------------------------------')
    print('5)Remover reclamação')
    print('--------------------------------------')
    print('6)Mostrar quantidade de reclamações')
    print('--------------------------------------')
    print('7)Sair do sistema')
    print('======================================')
    print(' ')
    print(' ')


    opcao=int(input('Escolha uma opção: '))

    if opcao==1:
        listar_reclamacoes()
       

    elif opcao==2:
        print('Nova reclamação')
        nova_reclamacao=input('Digite a reclamação:')
        reclamacoes.append(nova_reclamacao)
        print('Reclamação cadastrada com sucesso!')

    elif opcao==3:
        print('Pesquisar reclamação')
        codigo=int(input('Digite o ID da reclamação:'))-1

        if codigo>=0 and codigo<len(reclamacoes):
            print('Reclamação encontrada')
            print(reclamacoes[codigo])
        else:
            print('ID inválido')
    
    elif opcao==4:
        print('Atualizar reclamação')
        codigo=int(input('Digite o ID da reclamação:'))-1

        if codigo>=0 and codigo<len(reclamacoes):
            nova_descricao=input('Digite a nova descrição da reclamação:')
            reclamacoes[codigo]=nova_descricao
            print('Reclamação atualizada com sucesso!')
        else:
            print('ID inválido')

    elif opcao==5:
        print('Remover reclamação')
        codigo=int(input('Digite o ID da reclamação:'))-1

        if codigo>=0 and codigo< len(reclamacoes):
            reclamacoes.pop(codigo)
            print('Reclamação removida com sucesso!')
        
        else:
            print('ID inválido')

    elif opcao==6:
        print('Quantidade total de reclamações:',len(reclamacoes))

    elif opcao==7:
        print('Encerrando o sistema')
        sistema=False
    else:
        print('Opção inválida, tente novamente com as opções disponíveis')
