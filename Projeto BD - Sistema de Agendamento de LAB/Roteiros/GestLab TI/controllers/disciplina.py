from conexao import supabase

def listar_disciplinas():
    res = supabase.table("disciplina").select("*").execute()
    return res.data

def buscar_disciplina(id_disciplina):
    res = supabase.table("disciplina") \
        .select("*") \
        .eq("id_disciplina", id_disciplina) \
        .execute()

    return res.data[0] if res.data else None

def cadastrar_disciplina(nome, id_curso):
    res = supabase.table("disciplina").insert({
        "nome": nome,
        "id_curso": id_curso
    }).execute()
    return res.data

def excluir_disciplina(id_disciplina):
    res = supabase.table("disciplina") \
        .delete() \
        .eq("id_disciplina", id_disciplina) \
        .execute()

    return res.data

def vincular_professor(id_disciplina, cpf_professor):
    res = supabase.table("professor_disciplina").insert({
        "id_disciplina": id_disciplina,
        "cpf_professor": cpf_professor
    }).execute()

    return res.data