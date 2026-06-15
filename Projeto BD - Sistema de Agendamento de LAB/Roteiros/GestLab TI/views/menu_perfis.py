from views.display import titulo, tabela, pausar
from controllers import perfis as ctrl


def menu():
    while True:
        titulo("TIPOS DE USUÁRIOS")

        print("  1. Listar alunos")
        print("  2. Listar professores")
        print("  3. Listar monitores")
        print("  4. Listar técnicos")
        print("  0. Voltar")

        op = input("\n  Opção: ").strip()

        if op == "1":
            alunos()

        elif op == "2":
            professores()

        elif op == "3":
            monitores()

        elif op == "4":
            tecnicos()

        elif op == "0":
            break

def alunos():
    titulo("ALUNOS")

    dados = ctrl.listar_alunos()

    linhas = []

    for a in dados:
        linhas.append({
            "cpf": a["cpf_aluno"],
            "nome": a["usuario"]["nome"],
            "email": a["usuario"]["email"],
            "matricula": a["matricula"],
            "periodo": a["periodo"]
        })

    tabela(
        linhas,
        ["cpf", "nome", "email", "matricula", "periodo"],
        ["CPF", "Nome", "Email", "Matrícula", "Período"]
    )

    pausar()


def professores():
    titulo("PROFESSORES")

    dados = ctrl.listar_professores()

    linhas = []

    for p in dados:
        linhas.append({
            "cpf": p["cpf_professor"],
            "nome": p["usuario"]["nome"],
            "email": p["usuario"]["email"],
            "titulacao": p["titulacao"]
        })

    tabela(
        linhas,
        ["cpf", "nome", "email", "titulacao"],
        ["CPF", "Nome", "Email", "Titulação"]
    )

    pausar()


def monitores():
    titulo("MONITORES")

    dados = ctrl.listar_monitores()

    linhas = []

    for m in dados:
        linhas.append({
            "cpf": m["cpf_monitor"],
            "nome": m["usuario"]["nome"],
            "email": m["usuario"]["email"],
            "turno": m["turno"]
        })

    tabela(
        linhas,
        ["cpf", "nome", "email", "turno"],
        ["CPF", "Nome", "Email", "Turno"]
    )

    pausar()


def tecnicos():
    titulo("TÉCNICOS")

    dados = ctrl.listar_tecnicos()

    linhas = []

    for t in dados:
        linhas.append({
            "cpf": t["cpf_tecnico"],
            "nome": t["usuario"]["nome"],
            "email": t["usuario"]["email"],
            "cargo": t["cargo"]
        })

    tabela(
        linhas,
        ["cpf", "nome", "email", "cargo"],
        ["CPF", "Nome", "Email", "Cargo"]
    )

    pausar()