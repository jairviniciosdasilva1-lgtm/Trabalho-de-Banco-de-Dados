from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import manutencao as ctrl


TIPOS    = ["HARDWARE", "SOFTWARE", "REDE", "ENERGIA", "OUTRO"]
STATUS   = ["ABERTA", "EM_ANDAMENTO", "CONCLUIDA", "CANCELADA"]


def menu():
    while True:
        titulo("GESTÃO DE MANUTENÇÕES")
        print("  1. Listar manutenções")
        print("  2. Abrir manutenção")
        print("  3. Cancelar manutenção")
        print("  4. Atualizar status")
        print("  5. Listar equipamentos")
        print("  0. Voltar")
        op = input("\n  Opção: ").strip()

        if op == "1":
            listar()
        elif op == "2":
            abrir()
        elif op == "3":
            cancelar()
        elif op == "4":
            atualizar()
        elif op == "5":
            equipamentos()
        elif op == "0":
            break


def listar():
    titulo("MANUTENÇÕES")
    dados = ctrl.listar_manutencoes()
    tabela(dados,
           ["id_manutencao", "equipamento", "laboratorio", "tipo_problema", "status", "tecnico_responsavel"],
           ["ID", "Equipamento", "Laboratório", "Tipo", "Status", "Técnico"])
    pausar()


def abrir():
    titulo("ABRIR MANUTENÇÃO")
    descricao      = input("  Descrição do problema: ").strip()
    print("  Tipos:", ", ".join(f"{i+1}.{t}" for i, t in enumerate(TIPOS)))
    tipo_idx       = int(input("  Tipo: ").strip()) - 1
    id_equipamento = int(input("  ID do equipamento: ").strip())
    id_laboratorio = int(input("  ID do laboratório: ").strip())
    cpf_tecnico    = input("  CPF do técnico: ").strip()
    id_ocorrencia  = input("  ID da ocorrência (opcional, Enter para pular): ").strip()
    id_ocorrencia  = int(id_ocorrencia) if id_ocorrencia else None
    try:
        id_manut = ctrl.abrir_manutencao(descricao, TIPOS[tipo_idx], id_equipamento, id_laboratorio, cpf_tecnico, id_ocorrencia)
        sucesso(f"Manutenção #{id_manut} aberta! Equipamento marcado como EM_MANUTENCAO.")
    except Exception as e:
        erro(str(e))
    pausar()


def cancelar():
    titulo("CANCELAR MANUTENÇÃO")
    id_manutencao = int(input("  ID da manutenção: ").strip())
    motivo        = input("  Motivo do cancelamento: ").strip()
    try:
        ctrl.cancelar_manutencao(id_manutencao, motivo)
        sucesso("Manutenção cancelada!")
    except Exception as e:
        erro(str(e))
    pausar()


def atualizar():
    titulo("ATUALIZAR STATUS")
    id_manutencao = int(input("  ID da manutenção: ").strip())
    print("  Status:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(STATUS)))
    idx = int(input("  Novo status: ").strip()) - 1
    try:
        ctrl.atualizar_status(id_manutencao, STATUS[idx])
        sucesso("Status atualizado!")
    except Exception as e:
        erro(str(e))
    pausar()


def equipamentos():
    titulo("EQUIPAMENTOS")
    dados = ctrl.listar_equipamentos()
    tabela(dados,
           ["id_equipamento", "nome", "status", "id_laboratorio"],
           ["ID", "Nome", "Status", "ID Lab"])
    pausar()
