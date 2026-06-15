from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import laboratorio as ctrl


STATUS = ["ATIVO", "INATIVO", "EM_MANUTENCAO"]


def menu():
    while True:
        titulo("GESTÃO DE LABORATÓRIOS")
        print("  1. Listar laboratórios")
        print("  2. Status detalhado")
        print("  3. Cadastrar laboratório")
        print("  4. Atualizar status")
        print("  5. Verificar disponibilidade")
        print("  0. Voltar")
        op = input("\n  Opção: ").strip()

        if op == "1":
            listar()
        elif op == "2":
            status()
        elif op == "3":
            cadastrar()
        elif op == "4":
            atualizar()
        elif op == "5":
            disponibilidade()
        elif op == "0":
            break


def listar():
    titulo("LABORATÓRIOS")
    dados = ctrl.listar_laboratorios()
    tabela(dados,
           ["id_laboratorio", "nome", "bloco", "andar", "capacidade", "status"],
           ["ID", "Nome", "Bloco", "Andar", "Capacidade", "Status"])
    pausar()


def status():
    titulo("STATUS DOS LABORATÓRIOS")
    dados = ctrl.status_laboratorios()
    tabela(dados,
           ["nome", "status", "total_equipamentos", "equipamentos_ativos", "equipamentos_em_manutencao", "total_computadores"],
           ["Laboratório", "Status", "Total Equip.", "Ativos", "Em Manutenção", "Computadores"])
    pausar()


def cadastrar():
    titulo("CADASTRAR LABORATÓRIO")
    nome       = input("  Nome: ").strip()
    bloco      = input("  Bloco: ").strip()
    andar      = int(input("  Andar: ").strip())
    capacidade = int(input("  Capacidade: ").strip())
    try:
        ctrl.cadastrar_laboratorio(nome, bloco, andar, capacidade)
        sucesso("Laboratório cadastrado!")
    except Exception as e:
        erro(str(e))
    pausar()


def atualizar():
    titulo("ATUALIZAR STATUS")
    id_lab = int(input("  ID do laboratório: ").strip())
    print("  Status:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(STATUS)))
    idx = int(input("  Novo status: ").strip()) - 1
    try:
        ctrl.atualizar_status(id_lab, STATUS[idx])
        sucesso("Status atualizado!")
    except Exception as e:
        erro(str(e))
    pausar()


def disponibilidade():
    titulo("VERIFICAR DISPONIBILIDADE")
    id_lab    = int(input("  ID do laboratório: ").strip())
    data      = input("  Data (YYYY-MM-DD): ").strip()
    id_horario = int(input("  ID do horário: ").strip())
    try:
        disponivel = ctrl.verificar_disponibilidade(id_lab, data, id_horario)
        if disponivel:
            sucesso("Laboratório disponível nesse horário!")
        else:
            print("\n  ✗ Laboratório já reservado nesse horário.\n")
    except Exception as e:
        erro(str(e))
    pausar()
