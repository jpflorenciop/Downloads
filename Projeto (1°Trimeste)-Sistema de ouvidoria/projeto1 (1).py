# Ítalo Felipe | Rafael de Araujo | Samuel Nunes | João Pedro Florêncio

reclamacoes = []

def mostrar_menu():
    print("\n--- SISTEMA DE OUVIDORIA ---")
    print("1 - Listar reclamações")
    print("2 - Registrar nova reclamação")
    print("3 - Pesquisar reclamação")
    print("4 - Atualizar reclamação")
    print("5 - Remover reclamação")
    print("6 - Quantidade de reclamações")
    print("7 - Sair")


def registrar_reclamacao(codigo_atual):
    texto = input("Digite a reclamação: ")

    nova_reclamacao = {
        "codigo": codigo_atual,
        "texto": texto
    }

    reclamacoes.append(nova_reclamacao)
    print("Reclamação registrada com sucesso!")

    return codigo_atual + 1


def listar_reclamacoes():
    if not reclamacoes:
        print("Nenhuma reclamação encontrada.")
        return

    for r in reclamacoes:
        print(f"\nCódigo: {r['codigo']}")
        print(f"Reclamação: {r['texto']}")
        print("-" * 20)


def pesquisar_reclamacao():
    codigo_procurado = int(input("Digite o código da reclamação: "))

    for r in reclamacoes:
        if r["codigo"] == codigo_procurado:
            print("\nReclamação encontrada:")
            print(f"Código: {r['codigo']}")
            print(f"Texto: {r['texto']}")
            return

    print("Reclamação não encontrada.")


def atualizar_reclamacao():
    codigo_procurado = int(input("Digite o código da reclamação: "))

    for r in reclamacoes:
        if r["codigo"] == codigo_procurado:
            novo_texto = input("Digite a nova reclamação: ")
            r["texto"] = novo_texto
            print("Reclamação atualizada com sucesso!")
            return

    print("Código não encontrado.")


def remover_reclamacao():
    codigo_procurado = int(input("Digite o código da reclamação: "))

    for r in reclamacoes:
        if r["codigo"] == codigo_procurado:
            reclamacoes.remove(r)
            print("Reclamação removida com sucesso!")
            return

    print("Código não encontrado.")


def mostrar_total_reclamacoes():
    print("Total de reclamações:", len(reclamacoes))


def main():
    codigo = 1
    opcao = ""

    while opcao != "7":
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_reclamacoes()
        elif opcao == "2":
            codigo = registrar_reclamacao(codigo)
        elif opcao == "3":
            pesquisar_reclamacao()
        elif opcao == "4":
            atualizar_reclamacao()
        elif opcao == "5":
            remover_reclamacao()
        elif opcao == "6":
            mostrar_total_reclamacoes()
        elif opcao == "7":
            print("Encerrando sistema...")
        else:
            print("Opção inválida. Tente novamente.")


main()
