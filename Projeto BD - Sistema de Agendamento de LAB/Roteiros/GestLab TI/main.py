import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from views.display import titulo, pausar
from views import (
    menu_usuario,
    menu_laboratorio,
    menu_reserva,
    menu_ocorrencia,
    menu_manutencao,
    menu_computador,
    menu_disciplinas,
    menu_perfis
)
from controllers.auth import login


def relatorio_geral():
    from conexao import supabase
    from views.display import titulo, pausar

    titulo("RELATÓRIO GERAL DO SISTEMA")
    res = supabase.rpc("fn_relatorio_geral", {}).execute()

    if res.data:
        d = res.data[0]
        print(f"  Usuários:          {d['total_usuarios']}")
        print(f"    Alunos:          {d['total_alunos']}")
        print(f"    Professores:     {d['total_professores']}")
        print(f"    Monitores:       {d['total_monitores']}")
        print(f"    Técnicos:        {d['total_tecnicos']}")
        print()
        print(f"  Laboratórios:      {d['total_laboratorios']}")
        print(f"    Ativos:          {d['labs_ativos']}")
        print(f"    Em manutenção:   {d['labs_manutencao']}")
        print()
        print(f"  Equipamentos:      {d['total_equipamentos']}")
        print(f"    Ativos:          {d['equip_ativos']}")
        print(f"    Em manutenção:   {d['equip_manutencao']}")
        print()
        print(f"  Reservas pendentes:    {d['reservas_pendentes']}")
        print(f"  Reservas aprovadas:    {d['reservas_aprovadas']}")
        print(f"  Ocorrências abertas:   {d['ocorrencias_abertas']}")
        print(f"  Manutenções abertas:   {d['manutencoes_abertas']}")

    pausar()


def tela_login():
    while True:
        print("\n" + "-" * 60)
        print("  GESTLAB TI")
        print("-" * 60)
        print("  1. Login")
        print("  2. Cadastrar novo usuário")
        print("  0. Sair")

        op = input("\n  Opção: ").strip()

        if op == "0":
            print("\n  Saindo...\n")
            sys.exit()

        elif op == "2":
            menu_usuario.cadastrar()
            continue

        elif op == "1":
            print()
            email = input("  Email: ").strip()
            senha = input("  Senha: ").strip()

            usuario = login(email, senha)

            if usuario:
                print(f"\n  ✓ Bem-vindo, {usuario['nome']}!\n")
                return usuario

            print("\n  ✗ Email ou senha inválidos.\n")



def mostrar_menu(tipo):
    if tipo == "ALUNO":
        print("  5. Ocorrências")
        print("  0. Sair")

    elif tipo == "PROFESSOR":
        print("  4. Reservas")
        print("  5. Ocorrências")
        print("  0. Sair")

    elif tipo == "TECNICO":
        print("  6. Manutenções")
        print("  7. Computador")
        print("  5. Ocorrências")
        print("  0. Sair")

    elif tipo == "MONITOR":
        print("  3. Laboratórios")
        print("  5. Ocorrências")
        print("  0. Sair")


def main():
    usuario_logado = tela_login()
    tipo = usuario_logado["tipo_usuario"]


    permissoes = {
        "ALUNO": ["5", "0"],
        "PROFESSOR": ["4", "5", "0"],
        "TECNICO": ["6", "7", "5", "0"],
        "MONITOR": ["3", "5", "0"]
    }

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        titulo("GestLab TI — Sistema de Gerenciamento de Laboratórios")

        print(f"Usuário: {usuario_logado['nome']}")
        print(f"Perfil: {tipo}")
        print()

    
        mostrar_menu(tipo)

        op = input("\n  Opção: ").strip()


        if op not in permissoes.get(tipo, []):
            print("\n  ❌ Você não tem permissão para essa opção!")
            pausar()
            continue

    
        if op == "1":
            menu_usuario.menu()
        elif op == "2":
            menu_perfis.menu()
        elif op == "3":
            menu_laboratorio.menu()
        elif op == "4":
            menu_reserva.menu()
        elif op == "5":
            menu_ocorrencia.menu()
        elif op == "6":
            menu_manutencao.menu()
        elif op == "7":
            menu_computador.menu()
        elif op == "8":
            menu_disciplinas.menu()
        elif op == "9":
            relatorio_geral()
        elif op == "0":
            print("\n  Saindo do sistema...\n")
            break


if __name__ == "__main__":
    main()