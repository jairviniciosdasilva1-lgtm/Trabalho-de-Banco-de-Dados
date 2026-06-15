from conexao import supabase


def listar_computadores():
    res = supabase.table("computador").select("*").execute()
    return res.data


def cadastrar_computador(id_equipamento, sistema_operacional, numero_maquina):
    res = supabase.table("computador").insert({
        "id_equipamento": id_equipamento,
        "sistema_operacional": sistema_operacional,
        "numero_maquina": numero_maquina
    }).execute()
    return res.data