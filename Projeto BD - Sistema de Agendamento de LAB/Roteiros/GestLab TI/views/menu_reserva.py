from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import reserva as ctrl


STATUS = ["PENDENTE", "APROVADA", "CANCELADA", "CONCLUIDA"]


def menu():
    while True:
        titulo("GESTÃO DE RESERVAS")
        print("  1. Listar todas as reservas")
        print("  2. Buscar reservas por professor")
        print("  3. Criar reserva")
        print("  4. Atualizar status da reserva")
        print("  5. Listar horários disponíveis")
        print("  0. Voltar")
        op = input("\n  Opção: ").strip()

        if op == "1":
            listar()
        elif op == "2":
            por_professor()
        elif op == "3":
            criar()
        elif op == "4":
            atualizar()
        elif op == "5":
            horarios()
        elif op == "0":
            break


def listar():
    titulo("TODAS AS RESERVAS")
    dados = ctrl.listar_reservas()
    tabela(dados,
           ["id_reserva", "data_reserva", "laboratorio", "professor", "status", "finalidade"],
           ["ID", "Data", "Laboratório", "Professor", "Status", "Finalidade"])
    pausar()


def por_professor():
    titulo("RESERVAS POR PROFESSOR")
    cpf        = input("  CPF do professor: ").strip()
    data_inicio = input("  Data início (YYYY-MM-DD): ").strip()
    data_fim    = input("  Data fim (YYYY-MM-DD): ").strip()
    try:
        dados = ctrl.buscar_reservas_professor(cpf, data_inicio, data_fim)
        tabela(dados,
               ["id_reserva", "data_reserva", "laboratorio", "status", "finalidade"],
               ["ID", "Data", "Laboratório", "Status", "Finalidade"])
    except Exception as e:
        erro(str(e))
    pausar()


def criar():
    titulo("CRIAR RESERVA")
    data_reserva   = input("  Data (YYYY-MM-DD): ").strip()
    finalidade     = input("  Finalidade: ").strip()
    id_laboratorio = int(input("  ID do laboratório: ").strip())
    cpf_professor  = input("  CPF do professor: ").strip()
    id_disciplina  = input("  ID da disciplina (opcional, Enter para pular): ").strip()
    id_disciplina  = int(id_disciplina) if id_disciplina else None

    try:
        reserva = ctrl.criar_reserva(data_reserva, finalidade, id_laboratorio, cpf_professor, id_disciplina)
        if reserva:
            id_reserva = reserva["id_reserva"]
            sucesso(f"Reserva #{id_reserva} criada!")

            while True:
                id_horario = input("  Adicionar horário (ID) ou Enter para finalizar: ").strip()
                if not id_horario:
                    break
                ctrl.adicionar_horario_reserva(id_reserva, int(id_horario))
                sucesso(f"Horário {id_horario} adicionado.")
    except Exception as e:
        erro(str(e))
    pausar()


def atualizar():
    titulo("ATUALIZAR STATUS DA RESERVA")
    id_reserva = int(input("  ID da reserva: ").strip())
    print("  Status:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(STATUS)))
    idx = int(input("  Novo status: ").strip()) - 1
    try:
        ctrl.atualizar_status(id_reserva, STATUS[idx])
        sucesso("Status atualizado!")
    except Exception as e:
        erro(str(e))
    pausar()


def horarios():
    titulo("HORÁRIOS CADASTRADOS")
    dados = ctrl.listar_horarios()
    tabela(dados,
           ["id_horario", "hora_inicio", "hora_fim", "turno"],
           ["ID", "Início", "Fim", "Turno"])
    pausar()
