# Lista para armazenar os usuários
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o e-mail: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Lista de usuários:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")

# Função para buscar um usuário pelo nome
def buscar_usuario():
    nome_busca = input("Digite o nome do usuário para buscar: ").lower()
    encontrado = False
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca:
            print("Usuário encontrado:")
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
            encontrado = True
            break
    if not encontrado:
        print("Usuário não encontrado.")

# Função principal com menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário por nome")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
