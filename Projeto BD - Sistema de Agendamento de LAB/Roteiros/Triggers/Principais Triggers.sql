Principais Triggers
1: Impede reserva em laboratório em manutenção ou inativo
CREATE OR REPLACE FUNCTION trg_fn_validar_reserva()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
   v_status_lab status_lab_enum;
BEGIN
   SELECT status INTO v_status_lab
   FROM LABORATORIO
   WHERE id_laboratorio = NEW.id_laboratorio;
   IF v_status_lab <> 'ATIVO' THEN
       RAISE EXCEPTION
           'Não é possível reservar o laboratório %. Status atual: %',
           NEW.id_laboratorio, v_status_lab;
   END IF;
   RETURN NEW;
END;
$$;
CREATE TRIGGER trg_validar_reserva
BEFORE INSERT ON RESERVA
FOR EACH ROW
EXECUTE FUNCTION trg_fn_validar_reserva();

2: Toda vez que uma manutenção for concluída, reativa o equipamento automaticamente

CREATE OR REPLACE FUNCTION trg_fn_concluir_manutencao()
												
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
   IF NEW.status = 'CONCLUIDA' AND OLD.status <> 'CONCLUIDA' THEN
       -- Registra data de conclusão se não informada
       IF NEW.data_conclusao IS NULL THEN
           NEW.data_conclusao := CURRENT_TIMESTAMP;
       END IF;
       -- Reativa o equipamento
       UPDATE EQUIPAMENTO
       SET status = 'ATIVO'
       WHERE id_equipamento = NEW.id_equipamento;
   END IF;
   RETURN NEW;
END;
$$;
CREATE TRIGGER trg_concluir_manutencao
BEFORE UPDATE ON MANUTENCAO
FOR EACH ROW
EXECUTE FUNCTION trg_fn_concluir_manutencao();

3: Validação de usuário
CREATE OR REPLACE FUNCTION trg_fn_validar_usuario()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
   IF NEW.CPF !~ '^\d{3}\.\d{3}\.\d{3}-\d{2}$' THEN
       RAISE EXCEPTION 'CPF % inválido. Use o formato 000.000.000-00.', NEW.CPF;
   END IF;


   IF NEW.email !~ '^[^@]+@[^@]+\.[^@]+$' THEN
       RAISE EXCEPTION 'Email % inválido.', NEW.email;
   END IF;


   IF NEW.telefone !~ '^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$' THEN
       RAISE EXCEPTION 'Telefone % inválido.', NEW.telefone;
   END IF;


   RETURN NEW;
END;
$$;
												
CREATE TRIGGER trg_validar_usuario
BEFORE INSERT OR UPDATE ON USUARIO
FOR EACH ROW
EXECUTE FUNCTION trg_fn_validar_usuario();

4: Bloqueia conflito de horário em reservas
CREATE OR REPLACE FUNCTION trg_fn_conflito_horario()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
   v_conflito INT;
BEGIN
   SELECT COUNT(*) INTO v_conflito
   FROM RESERVA_HORARIO rh
   JOIN RESERVA r ON rh.id_reserva = r.id_reserva
   WHERE r.id_laboratorio = NEW.id_laboratorio
     AND r.data_reserva   = NEW.data_reserva
     AND rh.id_horario    = NEW.id_horario
     AND r.status IN ('PENDENTE', 'APROVADA')
     AND r.id_reserva    <> NEW.id_reserva;


   IF v_conflito > 0 THEN
       RAISE EXCEPTION 'Conflito de horário: laboratório % já reservado nesse horário.', NEW.id_laboratorio;
   END IF;


   RETURN NEW;
END;
$$;


CREATE TRIGGER trg_conflito_horario
BEFORE INSERT ON RESERVA_HORARIO
FOR EACH ROW
EXECUTE FUNCTION trg_fn_conflito_horario();
