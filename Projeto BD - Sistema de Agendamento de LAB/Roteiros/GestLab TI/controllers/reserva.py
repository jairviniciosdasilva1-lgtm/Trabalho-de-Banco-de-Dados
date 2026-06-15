from conexao import supabase


def listar_reservas():
    res = supabase.table("vw_reservas_detalhadas").select("*").execute()
    return res.data


def buscar_reservas_professor(cpf, data_inicio, data_fim):
    res = supabase.rpc("fn_reservas_professor", {
        "p_cpf_professor": cpf,
        "p_data_inicio": data_inicio,
        "p_data_fim": data_fim
    }).execute()
    return res.data


def criar_reserva(data_reserva, finalidade, id_laboratorio, cpf_professor, id_disciplina=None):
    res = supabase.table("reserva").insert({
        "data_reserva": data_reserva,
        "finalidade": finalidade,
        "id_laboratorio": id_laboratorio,
        "cpf_professor": cpf_professor,
        "id_disciplina": id_disciplina,
        "status": "PENDENTE"
    }).execute()
    return res.data[0] if res.data else None


def adicionar_horario_reserva(id_reserva, id_horario):
    res = supabase.table("reserva_horario").insert({
        "id_reserva": id_reserva,
        "id_horario": id_horario
    }).execute()
    return res.data


def atualizar_status(id_reserva, status):
    res = supabase.table("reserva").update({
        "status": status
    }).eq("id_reserva", id_reserva).execute()
    return res.data


def listar_horarios():
    res = supabase.table("horario").select("*").execute()
    return res.data
