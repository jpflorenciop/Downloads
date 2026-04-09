# opcao = 0
# identificador = 1000
# inventario = []
# itens_disponiveis = []

# while opcao != 7:
#     print("Menu")
#     print("1 - Cadastrar Equipamento")
#     print("2 - Listar Inventário")
#     print("3 - Pesquisar por Categoria")
#     print("4 - Atualizar Status")
#     print("5 - Remover Item")
#     print("6 - Relatório de Disponibilidade")
#     print("7 - Sair")

#     opcao = int(input("Qual opção você quer: "))

#     if opcao == 1:
#         id = identificador
#         nomeDigitado = input("Digite o nome do item: ")
#         categoriaDigitada = input("Digite a categoria do item: ")
#         statusInicial = "Disponivel"

#         identificador += 1

#         item = {
#             "id": identificador,
#             "nome": nomeDigitado,
#             "categoria": categoriaDigitada,
#             "status": statusInicial
#         }

#         inventario.append(item)

#         print("Equipamento registrado com sucesso!")
    
#     elif opcao == 2:
#         if len(inventario) == 0:
#             print("Não existe equipamento cadastrado")
#         else:
#             for item in inventario:
#                 print(f"Id: {item['id']} \nStatus: {item['status']}")
#                 print("_____________________________")
    
#     elif opcao == 3:
#         categoria_procurada = input("Digite a categoria procurada: ")
#         encontrou = False
#         for item in inventario:
#             if item["categoria"] == categoria_procurada:
#                 encontrou = True
#                 print(f"Nome: {item['nome']}. Status: {item['status']}")


#         if not encontrou:
#             print("Não há equipamento registrado nessa categoria.")

#     elif opcao == 4:
#         id_procurado = int(input("Digite o ID do produto procurado: "))
#         encontrou = False

#         for item in inventario:
#             if item["id"] == id_procurado:
#                 encontrou = True
#                 print(f"Produto Encontrado. O status atual é: {item['status']}")
#                 novo_status = input("Digite o novo status (Alocado ou Quebrado):")
#                 item["status"] = novo_status
    
#         if not encontrou:
#             print("Não há equipamento registrado com esse ID.")

#     elif opcao == 5:
#         encontrou = False
#         id_procurado = int(input("Digite o ID do produto procurado: "))
#         for item in inventario:
#             if item["id"] == id_procurado:
#                 encontrou = True
#                 inventario.remove(item)
#         if not encontrou:
#             print("Não há equipamento registrado com esse ID.")
    
#     elif opcao == 6:
#         for item in inventario:
#             if item["status"] == "Disponivel":
#                 itens_disponiveis.append(item)
        
#         print("Quantidade de itens disponíveis: ", len(itens_disponiveis))
#         for item_disponivel in itens_disponiveis:
#             print(item_disponivel["nome"])
