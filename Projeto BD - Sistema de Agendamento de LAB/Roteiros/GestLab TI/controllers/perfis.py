from conexao import supabase

def listar_alunos():
    res = supabase.table("aluno").select(
        "cpf_aluno, matricula, periodo, usuario(nome,email)"
    ).execute()

    return res.data

def listar_professores():
    res = supabase.table("professor").select(
        "cpf_professor, titulacao, usuario(nome,email)"
    ).execute()

    return res.data

def listar_monitores():
    res = supabase.table("monitor").select(
        "cpf_monitor, turno, usuario(nome,email)"
    ).execute()

    return res.data

def listar_tecnicos():
    res = supabase.table("tecnico").select(
        "cpf_tecnico, cargo, usuario(nome,email)"
    ).execute()

    return res.data

