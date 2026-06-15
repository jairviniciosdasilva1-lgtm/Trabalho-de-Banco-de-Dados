from conexao import supabase


def listar_manutencoes():
    res = supabase.table("vw_manutencoes").select("*").execute()
    return res.data


def abrir_manutencao(descricao, tipo_problema, id_equipamento, id_laboratorio, cpf_tecnico, id_ocorrencia=None):
    res = supabase.rpc("fn_abrir_manutencao", {
        "p_descricao": descricao,
        "p_tipo_problema": tipo_problema,
        "p_id_equipamento": id_equipamento,
        "p_id_laboratorio": id_laboratorio,
        "p_cpf_tecnico": cpf_tecnico,
        "p_id_ocorrencia": id_ocorrencia
    }).execute()
    return res.data


def cancelar_manutencao(id_manutencao, motivo):
    res = supabase.rpc("fn_cancelar_manutencao", {
        "p_id_manutencao": id_manutencao,
        "p_motivo": motivo
    }).execute()
    return res.data


def atualizar_status(id_manutencao, status):
    res = supabase.table("manutencao").update({
        "status": status
    }).eq("id_manutencao", id_manutencao).execute()
    return res.data


def listar_equipamentos():
    res = supabase.table("equipamento").select("*").execute()
    return res.data
