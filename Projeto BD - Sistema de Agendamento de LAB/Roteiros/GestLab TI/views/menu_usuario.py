from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import usuario as ctrl


TIPOS = ["ALUNO", "PROFESSOR", "TECNICO", "MONITOR"]
TITULACOES = ["GRADUADO", "ESPECIALISTA", "MESTRE", "DOUTOR", "POS_DOUTOR"]
CARGOS = ["TECNICO_TI", "TECNICO_ELETRICO", "TECNICO_REDES", "TECNICO_SUPORTE", "OUTRO"]
TURNOS = ["MANHA", "TARDE", "NOITE"]


def menu():
    while True:
        titulo("GESTÃO DE USUÁRIOS")
        print("  1. Listar todos os usuários")
        print("  2. Buscar usuário por CPF")
        print("  3. Cadastrar usuário")
        print("  4. Excluir usuário")
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
        elif op == "0":
            break


def listar():
    titulo("TODOS OS USUÁRIOS")
    dados = ctrl.listar_usuarios()
    tabela(dados,
           ["CPF", "nome", "email", "tipo_usuario"],
           ["CPF", "Nome", "Email", "Tipo"])
    pausar()


def buscar():
    titulo("BUSCAR USUÁRIO")
    cpf = input("  CPF (000.000.000-00): ").strip()
    try:
        dados = ctrl.buscar_usuario(cpf)
        if dados:
            tabela(dados, ["nome", "email", "tipo", "detalhe"], ["Nome", "Email", "Tipo", "Detalhe"])
        else:
            print("  Usuário não encontrado.")
    except Exception as e:
        erro(str(e))
    pausar()


def cadastrar():
    titulo("CADASTRAR USUÁRIO")
    cpf      = input("  CPF (000.000.000-00): ").strip()
    nome     = input("  Nome: ").strip()
    email    = input("  Email: ").strip()
    senha    = input("  Senha: ").strip()
    telefone = input("  Telefone: ").strip()

    print("\n  Tipos:", ", ".join(f"{i+1}.{t}" for i, t in enumerate(TIPOS)))
    tipo_idx = int(input("  Tipo: ").strip()) - 1
    tipo = TIPOS[tipo_idx]

    try:
        ctrl.cadastrar_usuario(cpf, nome, email, senha, telefone, tipo)

        if tipo == "ALUNO":
            matricula = input("  Matrícula: ").strip()
            periodo   = int(input("  Período: ").strip())
            id_curso  = int(input("  ID do Curso: ").strip())
            ctrl.cadastrar_aluno(cpf, matricula, periodo, id_curso)

        elif tipo == "PROFESSOR":
            print("\n  Titulações:", ", ".join(f"{i+1}.{t}" for i, t in enumerate(TITULACOES)))
            tit_idx = int(input("  Titulação: ").strip()) - 1
            ctrl.cadastrar_professor(cpf, TITULACOES[tit_idx])

        elif tipo == "TECNICO":
            print("\n  Cargos:", ", ".join(f"{i+1}.{c}" for i, c in enumerate(CARGOS)))
            cargo_idx = int(input("  Cargo: ").strip()) - 1
            ctrl.cadastrar_tecnico(cpf, CARGOS[cargo_idx])

        elif tipo == "MONITOR":
            print("\n  Turnos:", ", ".join(f"{i+1}.{t}" for i, t in enumerate(TURNOS)))
            turno_idx = int(input("  Turno: ").strip()) - 1
            ctrl.cadastrar_monitor(cpf, TURNOS[turno_idx])

        sucesso("Usuário cadastrado com sucesso!")
    except Exception as e:
        erro(str(e))
    pausar()


def excluir():
    titulo("EXCLUIR USUÁRIO")
    cpf = input("  CPF: ").strip()
    confirma = input(f"  Confirma exclusão de {cpf}? (s/n): ").strip().lower()
    if confirma == "s":
        try:
            ctrl.excluir_usuario(cpf)
            sucesso("Usuário excluído.")
        except Exception as e:
            erro(str(e))
    pausar()
