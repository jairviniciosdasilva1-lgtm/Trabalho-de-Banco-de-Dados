from conexao import supabase


def listar_usuarios():
    res = supabase.table("usuario").select("*").execute()
    return res.data


def buscar_usuario(cpf):
    res = supabase.rpc("fn_buscar_usuario", {"p_cpf": cpf}).execute()
    return res.data


def cadastrar_usuario(cpf, nome, email, senha, telefone, tipo):
    res = supabase.table("usuario").insert({
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "tipo_usuario": tipo
    }).execute()
    return res.data


def cadastrar_aluno(cpf, matricula, periodo, id_curso):
    res = supabase.table("aluno").insert({
        "cpf_aluno": cpf,
        "matricula": matricula,
        "periodo": periodo,
        "id_curso": id_curso
    }).execute()
    return res.data


def cadastrar_professor(cpf, titulacao):
    res = supabase.table("professor").insert({
        "cpf_professor": cpf,
        "especialidade": titulacao
    }).execute()
    return res.data


def cadastrar_tecnico(cpf, cargo):
    res = supabase.table("tecnico").insert({
        "cpf_tecnico": cpf,
        "cargo": cargo
    }).execute()
    return res.data


def cadastrar_monitor(cpf, turno):
    res = supabase.table("monitor").insert({
        "cpf_monitor": cpf,
        "turno": turno
    }).execute()
    return res.data


def excluir_usuario(cpf):
    res = supabase.table("usuario").delete().eq("cpf", cpf).execute()
    return res.data


def relatorio_usuarios():
    res = supabase.rpc("fn_usuarios_por_tipo", {"p_tipo": "ALUNO"}).execute()
    return res.data
