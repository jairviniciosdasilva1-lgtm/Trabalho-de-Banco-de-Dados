Principais Views
View 1: Laboratórios
CREATE VIEW vw_laboratorios_disponiveis AS
SELECT
id_laboratorio,
nome,
bloco,
andar,
capacidade
FROM laboratorio;

View 2: Reservas detalhadas
CREATE VIEW vw_reservas_detalhadas AS
SELECT
r.id_reserva,
r.data_reserva,
r.finalidade,
r.status,
l.nome AS laboratorio
FROM reserva r
JOIN laboratorio l
ON r.id_laboratorio = l.id_laboratorio;
												
View 3: Professor e disciplina
CREATE VIEW vw_professor_disciplina AS
SELECT
pd.cpf_professor,
d.nome AS disciplina
FROM professor_disciplina pd
JOIN disciplina d
ON pd.id_disciplina = d.id_disciplina;

View 4: Reservas por laboratório
CREATE VIEW vw_reservas_laboratorio AS
SELECT
l.nome AS laboratorio,
r.id_reserva,
r.data_reserva,
r.status
FROM laboratorio l
JOIN reserva r
ON l.id_laboratorio = r.id_laboratorio;

View 5: Quantidade de reservas por laboratório
CREATE VIEW vw_qtd_reservas_laboratorio AS
SELECT
l.nome,
COUNT(r.id_reserva) AS total_reservas
FROM laboratorio l
LEFT JOIN reserva r
ON l.id_laboratorio = r.id_laboratorio
GROUP BY l.nome;

View 6: Status dos laboratorios
CREATE OR REPLACE VIEW vw_laboratorios_status AS
SELECT
    l.nome,
    l.status,

												
    COUNT(DISTINCT e.id_equipamento) AS total_equipamentos,

    COUNT(DISTINCT CASE
        WHEN e.status = 'ATIVO'
        THEN e.id_equipamento
    END) AS equipamentos_ativos,

    COUNT(DISTINCT CASE
        WHEN e.status = 'EM_MANUTENCAO'
        THEN e.id_equipamento
    END) AS equipamentos_em_manutencao,

    COUNT(DISTINCT c.id_equipamento) AS total_computadores

FROM laboratorio l
LEFT JOIN equipamento e
    ON e.id_laboratorio = l.id_laboratorio
LEFT JOIN computador c
    ON c.id_equipamento = e.id_equipamento

GROUP BY
    l.id_laboratorio,
    l.nome,
    l.status;

7: Visualizar ocorrencia
CREATE OR REPLACE VIEW vw ocorrências abertas AS
SELECT
    o.id_ocorrencia,
    l.nome AS laboratorio,
    c.nome AS categoria,
    o.prioridade,
    o.status,
    u.nome AS autor
FROM ocorrência o
JOIN laboratório l
												
    ON l.id_laboratorio = o.id_laboratorio
JOIN categoria ocorrência c
    ON c.id_categoria = o.id_categoria
JOIN usuario u
    ONu.cpf = o.cpf autor
WHERE o.status = 'ABERTA';
