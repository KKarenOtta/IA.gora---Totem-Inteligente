# Totem FlexMedia - Sprint 1
# Programa para gerenciar informações de um totem interativo

# Lista para armazenar as informações (cada item é um dicionário)
informacoes = []

def cadastrar_informacao(lista):
    """
    Função para cadastrar uma nova informação na lista.
    Recebe título, tipo e descrição do usuário e adiciona à lista.
    """
    print("\n=== Cadastro de Informação ===")
    titulo = input("Digite o título: ")
    tipo = input("Digite o tipo (educativo, cultural, lazer, etc.): ")
    descricao = input("Digite a descrição: ")
    
    # Criando dicionário com as informações
    info = {
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    }
    
    # Adicionando à lista
    lista.append(info)
    print("\nInformação cadastrada com sucesso!")

def listar_informacoes(lista):
    """
    Função para listar todas as informações cadastradas.
    Exibe título, tipo e descrição de cada item na lista.
    """
    if not lista:
        print("\nNenhuma informação cadastrada.")
    else:
        print("\n=== Informações Cadastradas ===")
        for i, info in enumerate(lista, 1):
            print(f"\nRegistro {i}:")
            print(f"Título: {info['titulo']}")
            print(f"Tipo: {info['tipo']}")
            print(f"Descrição: {info['descricao']}")

def exibir_menu():
    """
    Função para exibir o menu inicial.
    """
    print("\n=== Totem FlexMedia ===")
    print("1 - Cadastrar informação")
    print("2 - Listar informações cadastradas")
    print("0 - Sair")

def main():
    """
    Função principal que controla o fluxo do programa.
    Utiliza um laço while para manter o menu ativo até a saída.
    """
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar_informacao(informacoes)
        elif opcao == "2":
            listar_informacoes(informacoes)
        elif opcao == "0":
            print("\nPrograma encerrado. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()