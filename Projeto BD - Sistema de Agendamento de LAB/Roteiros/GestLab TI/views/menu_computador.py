from views.display import titulo, tabela, sucesso, erro, pausar
from controllers import computador as ctrl_comp
from controllers import software as ctrl_soft


def menu():
    while True:
        titulo("GESTÃO DE COMPUTADORES")

        print("  1. Listar computadores")
        print("  2. Cadastrar computador")
        print("  3. Listar softwares")
        print("  4. Cadastrar software")
        print("  5. Instalar software")
        print("  6. Visualizar computador e seus softwares")
        print("  0. Voltar")

        op = input("\n  Opção: ").strip()

        if op == "1":
            listar_computadores()

        elif op == "2":
            cadastrar_computador()

        elif op == "3":
            listar_softwares()

        elif op == "4":
            cadastrar_software()

        elif op == "5":
            instalar_software()
        
        elif op == "6":
            softwares_instalados()

        elif op == "0":
            break


def listar_computadores():
    titulo("COMPUTADORES")

    dados = ctrl_comp.listar_computadores()

    tabela(
        dados,
        ["id_equipamento", "numero_maquina", "sistema_operacional"],
        ["ID", "Máquina", "Sistema Operacional"]
    )

    pausar()


def cadastrar_computador():
    titulo("CADASTRAR COMPUTADOR")

    id_equipamento = int(input("  ID do equipamento: "))
    sistema = input("  Sistema operacional: ")
    maquina = input("  Número da máquina: ")

    try:
        ctrl_comp.cadastrar_computador(
            id_equipamento,
            sistema,
            maquina
        )

        sucesso("Computador cadastrado!")

    except Exception as e:
        erro(str(e))

    pausar()


def listar_softwares():
    titulo("SOFTWARES")

    dados = ctrl_soft.listar_softwares()

    tabela(
        dados,
        ["id_software", "nome", "versao", "desenvolvedor"],
        ["ID", "Nome", "Versão", "Desenvolvedor"]
    )

    pausar()


def cadastrar_software():
    titulo("CADASTRAR SOFTWARE")

    nome = input("  Nome: ")
    versao = input("  Versão: ")
    desenvolvedor = input("  Desenvolvedor: ")

    try:
        ctrl_soft.cadastrar_software(
            nome,
            versao,
            desenvolvedor
        )

        sucesso("Software cadastrado!")

    except Exception as e:
        erro(str(e))

    pausar()


def instalar_software():
    titulo("INSTALAR SOFTWARE")

    id_equipamento = int(input("  ID do computador: "))
    id_software = int(input("  ID do software: "))

    try:
        ctrl_soft.instalar_software(
            id_equipamento,
            id_software
        )

        sucesso("Software instalado!")

    except Exception as e:
        erro(str(e))

    pausar()

def softwares_instalados():
    titulo("SOFTWARES INSTALADOS")

    dados = ctrl_soft.listar_softwares_instalados()

    tabela(
        dados,
        [
            "numero_maquina",
            "sistema_operacional",
            "software",
            "versao"
        ],
        [
            "Computador",
            "SO",
            "Software",
            "Versão"
        ]
    )

    pausar()