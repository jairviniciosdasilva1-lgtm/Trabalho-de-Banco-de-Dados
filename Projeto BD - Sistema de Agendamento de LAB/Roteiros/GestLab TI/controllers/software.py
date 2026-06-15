from conexao import supabase


def listar_softwares():
    res = supabase.table("software").select("*").execute()
    return res.data


def cadastrar_software(nome, versao, desenvolvedor):
    res = supabase.table("software").insert({
        "nome": nome,
        "versao": versao,
        "desenvolvedor": desenvolvedor
    }).execute()
    return res.data


def instalar_software(id_equipamento, id_software):
    res = supabase.table("computador_software").insert({
        "id_equipamento": id_equipamento,
        "id_software": id_software
    }).execute()

    return res.data

def listar_softwares_instalados():
    res = supabase.table(
        "vw_computadores_softwares"
    ).select("*").execute()

    return res.data