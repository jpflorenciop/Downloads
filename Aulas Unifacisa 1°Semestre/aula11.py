inventario = []
from operaçõesbd import * 
def listarItensDisponiveis():
    itens_disponiveis = []
    for item in inventario:
        if item["status"] == "Disponivel":
            itens_disponiveis.append(item)
        
    print("Quantidade de itens disponíveis: ", len(itens_disponiveis))
    for item_disponivel in itens_disponiveis:
        print(item_disponivel["nome"])

def removerItemId():
    encontrou = False
    id_procurado = int(input("Digite o ID do produto procurado: "))
    for item in inventario:
        if item["id"] == id_procurado:
            encontrou = True
            inventario.remove(item)
    if not encontrou:
        print("Não há equipamento registrado com esse ID.")

def atualizarStatus():
    id_procurado = int(input("Digite o ID do produto procurado: "))
    encontrou = False

    for item in inventario:
        if item["id"] == id_procurado:
            encontrou = True
            print(f"Produto Encontrado. O status atual é: {item['status']}")
            novo_status = input("Digite o novo status (Alocado ou Quebrado):")
            item["status"] = novo_status

    if not encontrou:
        print("Não há equipamento registrado com esse ID.")

def procurarPorCategoria():
    categoria_procurada = input("Digite a categoria procurada: ")
    encontrou = False
    for item in inventario:
        if item["categoria"] == categoria_procurada:
            encontrou = True
            print(f"Nome: {item['nome']}. Status: {item['status']}")


    if not encontrou:
        print("Não há equipamento registrado nessa categoria.")

def listarInventario():
    if len(inventario) == 0:
        print("Não existe equipamento cadastrado")
    else:
        for item in inventario:
            print(f"Id: {item['id']} \nStatus: {item['status']}")
            print("_____________________________")

def cadastrarEquipamento(identificador):
    
    
    id = identificador
    nomeDigitado = input("Digite o nome do item: ")
    categoriaDigitada = input("Digite a categoria do item: ")
    statusInicial = "Disponivel"

    identificador += 1

    item = {
        "id": id,
        "nome": nomeDigitado,
        "categoria": categoriaDigitada,
        "status": statusInicial
    }

    inventario.append(item)

    print("Equipamento registrado com sucesso!")

    return identificador

def menu():
    print("Menu")
    print("1 - Cadastrar Equipamento")
    print("2 - Listar Inventário")
    print("3 - Pesquisar por Categoria")
    print("4 - Atualizar Status")
    print("5 - Remover Item")
    print("6 - Relatório de Disponibilidade")
    print("7 - Sair")

    opcao = int(input("Qual opção você quer: "))

    return opcao

def main():
    conexao = criarConexao('localhost','root','S4lahking!','sistema_inventario')
    print(conexao)
    opcao = 0
    identificador = 1000
    while opcao != 7:
        opcao = menu()
        if opcao == 1:
            identificador = cadastrarEquipamento(identificador)
        elif opcao == 2:
            listarInventario()
        elif opcao == 3:
            procurarPorCategoria()

        elif opcao == 4:
            atualizarStatus()

        elif opcao == 5:
            removerItemId()
        
        elif opcao == 6:
            listarItensDisponiveis()

main()