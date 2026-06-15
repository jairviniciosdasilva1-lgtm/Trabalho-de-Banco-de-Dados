1: Verifica se um laboratório está disponível e um horário específico
CREATE OR REPLACE FUNCTION fn_laboratorio_disponivel(
   p_id_laboratorio INT,
   p_data           DATE,
   p_id_horario     INT
)       
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
   v_conflito INT;
BEGIN
   SELECT COUNT(*)
   INTO v_conflito
   FROM RESERVA r
   JOIN RESERVA_HORARIO rh ON r.id_reserva = rh.id_reserva
   WHERE r.id_laboratorio = p_id_laboratorio
     AND r.data_reserva   = p_data
     AND rh.id_horario    = p_id_horario
     AND r.status IN ('PENDENTE', 'APROVADA');
 
   RETURN v_conflito = 0;
END;
$$;
Como chamar a função: SELECT fn_laboratorio_disponivel (2, 26-08-12, 2);

2: Retorna o total de reservas de um professor e um intervalo de tempo
CREATE OR REPLACE FUNCTION fn_reservas_professor(
   p_cpf_professor CHAR(14),
   p_data_inicio   DATE,
   p_data_fim      DATE
)
RETURNS TABLE (
   id_reserva   INT,
   data_reserva DATE,
												
   status       status_reserva_enum,
   laboratorio  VARCHAR,
   finalidade   VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
   RETURN QUERY
   SELECT
       r.id_reserva,
       r.data_reserva,
       r.status,
       l.nome::VARCHAR AS laboratorio,
       r.finalidade::VARCHAR
   FROM RESERVA r
   JOIN LABORATORIO l ON r.id_laboratorio = l.id_laboratorio
   WHERE r.cpf_professor = p_cpf_professor
     AND r.data_reserva BETWEEN p_data_inicio AND p_data_fim
   ORDER BY r.data_reserva;
END;
$$;
Como chamar a função: SELECT * FROM fn_reservas_professor('222.222.222-22', '2025-01-01', '2025-12-31');

3: Retorna um resumo de ocorrências
CREATE OR REPLACE FUNCTION fn_resumo_ocorrencias(
   p_id_laboratorio INT
)
RETURNS TABLE (
   status       status_ocorr_enum,
   total        BIGINT,
   mais_recente TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
   IF NOT EXISTS (
       SELECT 1 FROM LABORATORIO WHERE id_laboratorio = p_id_laboratorio
   ) THEN
       RAISE EXCEPTION 'Laboratório % não encontrado.', p_id_laboratorio;
   END IF;


   RETURN QUERY
												
   SELECT
       o.status,
       COUNT(*)          AS total,
       MAX(o.data_ocorrencia) AS mais_recente
   FROM OCORRENCIA o
   WHERE o.id_laboratorio = p_id_laboratorio
   GROUP BY o.status
   ORDER BY total DESC;
END;
$$;
Como chamar a função: SELECT * FROM fn_resumo_ocorrencias(1);

4: Troca o tipo de usuário
CREATE OR REPLACE FUNCTION fn_trocar_tipo_usuario(
   p_cpf      CHAR(14),
   p_novo_tipo tipo_usuario_enum
)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
DECLARE
   v_tipo_atual tipo_usuario_enum;
BEGIN
   SELECT tipo_usuario INTO v_tipo_atual
   FROM USUARIO
   WHERE CPF = p_cpf;


   IF NOT FOUND THEN
       RAISE EXCEPTION 'Usuário % não encontrado.', p_cpf;
   END IF;


   IF v_tipo_atual = p_novo_tipo THEN
       RAISE EXCEPTION 'Usuário já é %.', p_novo_tipo;
   END IF;


   DELETE FROM ALUNO     WHERE cpf_aluno     = p_cpf;
   DELETE FROM PROFESSOR WHERE cpf_professor = p_cpf;
   DELETE FROM MONITOR   WHERE cpf_monitor   = p_cpf;
   DELETE FROM TECNICO   WHERE cpf_tecnico   = p_cpf;


   UPDATE USUARIO
   SET tipo_usuario = p_novo_tipo
   WHERE CPF = p_cpf;
												
   RETURN 'Tipo alterado de ' || v_tipo_atual || ' para ' || p_novo_tipo;
END;
$$;
Como chamar a função: SELECT fn_trocar_tipo_usuario('123.456.789-00', 'PROFESSOR');

5: Relatório geral
CREATE OR REPLACE FUNCTION fn_relatorio_geral()
RETURNS TABLE (
   total_usuarios      BIGINT,
   total_alunos        BIGINT,
   total_professores   BIGINT,
   total_monitores     BIGINT,
   total_tecnicos      BIGINT,
   total_laboratorios  BIGINT,
   labs_ativos         BIGINT,
   labs_manutencao     BIGINT,
   total_equipamentos  BIGINT,
   equip_ativos        BIGINT,
   equip_manutencao    BIGINT,
   reservas_pendentes  BIGINT,
   reservas_aprovadas  BIGINT,
   ocorrencias_abertas BIGINT,
   manutencoes_abertas BIGINT
)
LANGUAGE plpgsql
AS $$
BEGIN
   RETURN QUERY
   SELECT
       (SELECT COUNT(*) FROM USUARIO)                                              AS total_usuarios,
       (SELECT COUNT(*) FROM ALUNO)                                                AS total_alunos,
       (SELECT COUNT(*) FROM PROFESSOR)                                            AS total_professores,
       (SELECT COUNT(*) FROM MONITOR)                                              AS total_monitores,
       (SELECT COUNT(*) FROM TECNICO)                                              AS total_tecnicos,
       (SELECT COUNT(*) FROM LABORATORIO)                                          AS total_laboratorios,
       (SELECT COUNT(*) FROM LABORATORIO WHERE status = 'ATIVO')                  AS labs_ativos,
       (SELECT COUNT(*) FROM LABORATORIO WHERE status = 'EM_MANUTENCAO')          AS labs_manutencao,
       (SELECT COUNT(*) FROM EQUIPAMENTO)                                          AS total_equipamentos,
       (SELECT COUNT(*) FROM EQUIPAMENTO WHERE status = 'ATIVO')                  AS equip_ativos,
       (SELECT COUNT(*) FROM EQUIPAMENTO WHERE status = 'EM_MANUTENCAO')          AS equip_manutencao,
												25
       (SELECT COUNT(*) FROM RESERVA WHERE status = 'PENDENTE')                   AS reservas_pendentes,
       (SELECT COUNT(*) FROM RESERVA WHERE status = 'APROVADA')                   AS reservas_aprovadas,
       (SELECT COUNT(*) FROM OCORRENCIA WHERE status IN ('ABERTA','EM_ANDAMENTO')) AS ocorrencias_abertas,
       (SELECT COUNT(*) FROM MANUTENCAO WHERE status IN ('ABERTA','EM_ANDAMENTO')) AS manutencoes_abertas;
END;
$$;
Como chamar a função: SELECT * FROM fn_relatorio_geral();
