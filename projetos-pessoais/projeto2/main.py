# Lista de tarefas
tarefas = []

# Adiciona nova tarefa
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    tarefa = {
        "nome": nome,
        "concluida": False
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Lista todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['nome']} [{status}]")

# Marca uma tarefa como concluída
def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            num = int(input("Digite o número da tarefa concluída: "))
            if 1 <= num <= len(tarefas):
                tarefas[num - 1]["concluida"] = True
                print("Tarefa marcada como concluída.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

# Remove uma tarefa
def remover_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            num = int(input("Digite o número da tarefa a remover: "))
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                print(f"Tarefa '{removida['nome']}' removida com sucesso.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

# Menu principal
def menu():
    while True:
        print("\n--- Menu de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
