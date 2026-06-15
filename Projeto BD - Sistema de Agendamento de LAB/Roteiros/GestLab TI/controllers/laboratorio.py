from conexao import supabase


def listar_laboratorios():
    res = supabase.table("laboratorio").select("*").execute()
    return res.data


def buscar_laboratorio(id_lab):
    res = supabase.table("laboratorio").select("*").eq("id_laboratorio", id_lab).execute()
    return res.data[0] if res.data else None


def cadastrar_laboratorio(nome, bloco, andar, capacidade):
    res = supabase.table("laboratorio").insert({
        "nome": nome,
        "bloco": bloco,
        "andar": andar,
        "capacidade": capacidade,
        "status": "ATIVO"
    }).execute()
    return res.data


def atualizar_status(id_lab, status):
    res = supabase.table("laboratorio").update({
        "status": status
    }).eq("id_laboratorio", id_lab).execute()
    return res.data


def status_laboratorios():
    res = supabase.table("vw_laboratorios_status").select("*").execute()
    return res.data


def verificar_disponibilidade(id_lab, data, id_horario):
    res = supabase.rpc("fn_laboratorio_disponivel", {
        "p_id_laboratorio": id_lab,
        "p_data": data,
        "p_id_horario": id_horario
    }).execute()
    return res.data
