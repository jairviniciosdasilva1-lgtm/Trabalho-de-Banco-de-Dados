from conexao import supabase


def listar_ocorrencias():
    res = supabase.table("vw_ocorrencias_abertas").select("*").execute()
    return res.data


def resumo_ocorrencias(id_laboratorio):
    res = supabase.rpc("fn_resumo_ocorrencias", {
        "p_id_laboratorio": id_laboratorio
    }).execute()
    return res.data


def registrar_ocorrencia(descricao, prioridade, id_laboratorio, id_categoria, cpf_autor):
    res = supabase.table("ocorrencia").insert({
        "descricao": descricao,
        "prioridade": prioridade,
        "id_laboratorio": id_laboratorio,
        "id_categoria": id_categoria,
        "cpf_autor": cpf_autor,
        "status": "ABERTA"
    }).execute()
    return res.data


def escalar_prioridade(id_ocorrencia):
    res = supabase.rpc("fn_escalar_prioridade", {
        "p_id_ocorrencia": id_ocorrencia
    }).execute()
    return res.data


def atualizar_status(id_ocorrencia, status):
    res = supabase.table("ocorrencia").update({
        "status": status
    }).eq("id_ocorrencia", id_ocorrencia).execute()
    return res.data


def listar_categorias():
    res = supabase.table("categoria_ocorrencia").select("*").execute()
    return res.data
