
import csv

ARQUIVO_CSV = 'alunos.csv'


ARQUIVO_CSV = 'alunos.csv'


def cadastrar_aluno():
    while True:
        nome = input("Digite o nome do aluno: ")

        if not nome.isalpha():
            print("Nome inválido! Por favor, digite apenas letras.")
            continue

        idade = input("Digite a idade do aluno: ")
        if not idade.isdigit():
            print("Idade inválida! Por favor, digite apenas números.")
            continue

        endereco = input("Digite o endereço do aluno: ")

        curso = input("Digite o curso desejado do aluno: ")

        if "Inglês" not in curso and "Ingles" not in curso and "inglês" not in curso and "ingles" not in curso and "Espanhol" not in curso and "espanhol" not in curso:
            print(
                "Curso não cadastrado! Por favor, selecione o curso de Inglês ou de Espanhol")
            continue

        email = input("Digite o email do aluno: ")

        if "@gmail" not in email or "@hotmail" in email:
            print("Email inválido! Por favor, insira um email válido")
            continue

        aluno = [nome, idade, endereco, curso, email]

        try:
            with open(ARQUIVO_CSV, 'a', newline='') as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(aluno)
            print("Aluno cadastrado com sucesso!")
            break
        except IOError:
            print("Erro ao cadastrar o aluno.")
            break


def listar_alunos():
    try:
        with open(ARQUIVO_CSV, 'r') as arquivo:
            reader = csv.reader(arquivo)
            header = next(reader)  # Lê o cabeçalho do CSV

            for linha in reader:
                print(
                    f"Nome: {linha[0]}, Idade: {linha[1]}, Endereço: {linha[2]}, Curso Desejado: {linha[3]}, Email: {linha[4]}")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")


def excluir_aluno():
    nome = input("Digite o nome do aluno que deseja excluir: ")

    alunos = []
    removido = False

    try:
        with open(ARQUIVO_CSV, 'r') as arquivo:
            reader = csv.reader(arquivo)
            alunos = list(reader)

            for aluno in alunos:
                if aluno[0].lower() == nome.lower():
                    alunos.remove(aluno)
                    removido = True
                    break
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")

    if removido:
        try:
            with open(ARQUIVO_CSV, 'w', newline='') as arquivo:
                writer = csv.writer(arquivo)
                # Reescreve o cabeçalho
                writer.writerow(['Nome', 'Idade', 'Endereço',
                                'Curso Desejado', 'Email'])
                writer.writerows(alunos)

            print("Aluno removido com sucesso!")
        except IOError:
            print("Erro ao excluir o aluno.")
    else:
        print("Aluno não encontrado.")


def menu():
    while True:
        print("----- MENU -----")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Excluir aluno")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            excluir_aluno()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    menu()
