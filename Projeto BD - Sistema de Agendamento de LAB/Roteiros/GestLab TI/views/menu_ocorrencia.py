from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import ocorrencia as ctrl


PRIORIDADES = ["BAIXA", "MEDIA", "ALTA", "CRITICA"]
STATUS      = ["ABERTA", "EM_ANDAMENTO", "RESOLVIDA", "FECHADA"]


def menu():
    while True:
        titulo("GESTÃO DE OCORRÊNCIAS")
        print("  1. Listar ocorrências abertas")
        print("  2. Resumo por laboratório")
        print("  3. Registrar ocorrência")
        print("  4. Escalar prioridade")
        print("  5. Atualizar status")
        print("  0. Voltar")
        op = input("\n  Opção: ").strip()

        if op == "1":
            listar()
        elif op == "2":
            resumo()
        elif op == "3":
            registrar()
        elif op == "4":
            escalar()
        elif op == "5":
            atualizar()
        elif op == "0":
            break


def listar():
    titulo("OCORRÊNCIAS ABERTAS")
    dados = ctrl.listar_ocorrencias()
    tabela(dados,
           ["id_ocorrencia", "laboratorio", "categoria", "prioridade", "status", "autor"],
           ["ID", "Laboratório", "Categoria", "Prioridade", "Status", "Autor"])
    pausar()


def resumo():
    titulo("RESUMO DE OCORRÊNCIAS")
    id_lab = int(input("  ID do laboratório: ").strip())
    try:
        dados = ctrl.resumo_ocorrencias(id_lab)
        tabela(dados,
               ["status", "total", "mais_recente"],
               ["Status", "Total", "Mais Recente"])
    except Exception as e:
        erro(str(e))
    pausar()


def registrar():
    titulo("REGISTRAR OCORRÊNCIA")
    descricao      = input("  Descrição: ").strip()
    print("  Prioridades:", ", ".join(f"{i+1}.{p}" for i, p in enumerate(PRIORIDADES)))
    prio_idx       = int(input("  Prioridade: ").strip()) - 1
    id_laboratorio = int(input("  ID do laboratório: ").strip())
    id_categoria   = int(input("  ID da categoria: ").strip())
    cpf_autor      = input("  CPF do autor: ").strip()
    try:
        ctrl.registrar_ocorrencia(descricao, PRIORIDADES[prio_idx], id_laboratorio, id_categoria, cpf_autor)
        sucesso("Ocorrência registrada!")
    except Exception as e:
        erro(str(e))
    pausar()


def escalar():
    titulo("ESCALAR PRIORIDADE")
    id_ocorrencia = int(input("  ID da ocorrência: ").strip())
    try:
        resultado = ctrl.escalar_prioridade(id_ocorrencia)
        sucesso(resultado)
    except Exception as e:
        erro(str(e))
    pausar()


def atualizar():
    titulo("ATUALIZAR STATUS")
    id_ocorrencia = int(input("  ID da ocorrência: ").strip())
    print("  Status:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(STATUS)))
    idx = int(input("  Novo status: ").strip()) - 1
    try:
        ctrl.atualizar_status(id_ocorrencia, STATUS[idx])
        sucesso("Status atualizado!")
    except Exception as e:
        erro(str(e))
    pausar()
