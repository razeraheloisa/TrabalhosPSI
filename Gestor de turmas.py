turmas = {}
alunos = {}
presencas = []
notas = []

def cadastrar_turma():
    id_turma = input("ID da turma: ")
    nome = input("Nome da turma: ")
    professor = input("Professor: ")
    horario = input("Horário: ")

    turmas[id_turma] = {
        "nome": nome,
        "professor": professor,
        "horario": horario
    }
    print("Turma cadastrada com sucesso!\n")

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    id_aluno = input("ID do aluno: ")
    id_turma = input("ID da turma: ")

    if id_turma not in turmas:
        print("Turma não existe!\n")
        return

    alunos[id_aluno] = {
        "nome": nome,
        "turma": id_turma
    }
    print("Aluno cadastrado com sucesso!\n")

# Função unificada para registrar presença ou falta com validação de data
def registrar_presenca_ou_falta():
    id_aluno = input("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    # Validação da data no formato dd/mm
    while True:
        data = input("Data (dd/mm): ")
        if len(data) != 5 or data[2] != '/' or not data[:2].isdigit() or not data[3:].isdigit():
            print("Formato inválido! Use dd/mm (ex: 09/02).")
        else:
            break

    presente = input("O aluno esteve presente? (s/n): ").lower() == "s"

    tipo_falta = None
    if not presente:
        print("Tipo de falta:")
        print("1 - Justificada")
        print("2 - Injustificada")
        print("3 - Disciplinar")
        opcao = input("Escolha: ")

        if opcao == "1":
            tipo_falta = "justificada"
        elif opcao == "2":
            tipo_falta = "injustificada"
        elif opcao == "3":
            tipo_falta = "disciplinar"
        else:
            print("Tipo inválido!\n")
            return

    presencas.append({
        "aluno": id_aluno,
        "data": data,
        "presente": presente,
        "tipo_falta": tipo_falta
    })
    print("Registro concluído!\n")

def registrar_nota():
    id_aluno = input("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    avaliacao = input("Nome da avaliação: ")

    while True:
        nota = float(input("Nota: "))
        if nota < 0:
            print("digite uma nota maior")
        elif nota > 100:
            print("digite uma nota menor")

        return

    notas.append({
        "aluno": id_aluno,
        "avaliacao": avaliacao,
        "nota": nota
    })
    print("Nota registrada!\n")

def listar_alunos_turma():
    id_turma = input("ID da turma: ")

    print("\nAlunos da turma:")
    for id_aluno, dados in alunos.items():
        if dados["turma"] == id_turma:
            print(f"- {dados['nome']} (ID: {id_aluno})")
    print()

def relatorio_faltas_aluno():
    id_aluno = input("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    justificadas = 0
    injustificadas = 0
    disciplinares = 0

    for p in presencas:
        if p["aluno"] == id_aluno and not p["presente"]:
            if p["tipo_falta"] == "justificada":
                justificadas += 1
            elif p["tipo_falta"] == "injustificada":
                injustificadas += 1
            elif p["tipo_falta"] == "disciplinar":
                disciplinares += 1

    total_faltas = justificadas + injustificadas + disciplinares
    nome_aluno = alunos[id_aluno]["nome"]

    print("\n=== RELATÓRIO DE FALTAS ===")
    print(f"Aluno: {nome_aluno}")
    print(f"Total de faltas: {total_faltas}")
    print(f"Faltas justificadas: {justificadas}")
    print(f"Faltas injustificadas: {injustificadas}")
    print(f"Faltas disciplinares: {disciplinares}\n")

def menu():
    while True:
        print("=== GESTOR DE TURMAS ===")
        print("1 - Cadastrar turma")
        print("2 - Cadastrar aluno")
        print("3 - Registrar presença/falta")
        print("4 - Registrar nota")
        print("5 - Listar alunos por turma")
        print("6 - Relatório de faltas do aluno")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_turma()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            registrar_presenca_ou_falta()
        elif opcao == "4":
            registrar_nota()
        elif opcao == "5":
            listar_alunos_turma()
        elif opcao == "6":
            relatorio_faltas_aluno()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!\n")

menu()
