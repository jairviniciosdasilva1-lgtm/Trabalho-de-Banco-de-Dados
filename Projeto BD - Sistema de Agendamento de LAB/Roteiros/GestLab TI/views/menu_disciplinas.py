from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import disciplina as ctrl

def menu():
    while True:
        titulo("GESTÃO DE DISCIPLINAS")

        print("  1. Listar disciplinas")
        print("  2. Buscar disciplina")
        print("  3. Cadastrar disciplina")
        print("  4. Excluir disciplina")
        print("  5. Vincular professor")
        print("  0. Voltar")

        op = input("\n  Opção: ").strip()

        if op == "1":
            listar()

        elif op == "2":
            buscar()

        elif op == "3":
            cadastrar()

        elif op == "4":
            excluir()

        elif op == "5":
            vincular_professor()

        elif op == "0":
            break
        
def listar():
    titulo("DISCIPLINAS")

    dados = ctrl.listar_disciplinas()

    tabela(
        dados,
        ["id_disciplina", "nome", "id_curso"],
        ["ID", "Nome", "Curso"]
    )

    pausar()

def buscar():
    titulo("BUSCAR DISCIPLINA")

    id_disciplina = int(
        input("  ID da disciplina: ").strip()
    )

    dados = ctrl.buscar_disciplina(id_disciplina)

    if dados:
        tabela(
            [dados],
            ["id_disciplina", "nome", "id_curso"],
            ["ID", "Nome", "Curso"]
        )
    else:
        erro("Disciplina não encontrada.")

    pausar()

def cadastrar():
    titulo("CADASTRAR DISCIPLINA")

    nome = input("  Nome: ").strip()

    id_curso = int(
        input("  ID do curso: ").strip()
    )

    try:
        ctrl.cadastrar_disciplina(
            nome,
            id_curso
        )

        sucesso("Disciplina cadastrada!")

    except Exception as e:
        erro(str(e))

    pausar()

def excluir():
    titulo("EXCLUIR DISCIPLINA")

    id_disciplina = int(
        input("  ID da disciplina: ").strip()
    )

    try:
        ctrl.excluir_disciplina(id_disciplina)
        sucesso("Disciplina excluída!")

    except Exception as e:
        erro(str(e))

    pausar()

def vincular_professor():
    titulo("VINCULAR PROFESSOR")

    id_disciplina = int(
        input("  ID da disciplina: ").strip()
    )

    cpf_professor = input(
        "  CPF do professor: "
    ).strip()

    try:
        ctrl.vincular_professor(
            id_disciplina,
            cpf_professor
        )

        sucesso("Professor vinculado!")

    except Exception as e:
        erro(str(e))

    pausar()