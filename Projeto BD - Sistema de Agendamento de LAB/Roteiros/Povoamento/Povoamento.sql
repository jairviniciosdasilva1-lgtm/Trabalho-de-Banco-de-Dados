Povoamento
Tabela Usuário
INSERT INTO USUARIO (CPF, nome, email, senha, telefone, tipo_usuario) VALUES
('167.826.000-64', 'Andrisson Heitor', 'andrisson5533@gmail.com', 'Heitor0101@', '(84) 997877634', 'ALUNO'),
												
('180.800.000-12', 'Lucas Silva', 'lucassilva555@gmail.com', 'Lucas555silva', '(84) 991208080', 'PROFESSOR'),
('120.001.090-34', 'Maria Beatriz', 'beatriz005@gmail.com', 'beatriz005@', '(84) 99602-0000', 'MONITOR'),
('700.800.900-01', 'Ricardo Sousa', 'ricardo000@gmail.com', 'sousa0808@', '(84) 99000-5555', 'TECNICO'),
('100.200.300-22', 'Emanoel Melo', 'melo000@gmail.com', 'melo0000@', '(84) 99000-5508', 'PROFESSOR'),
('900.456.789-99', 'Luiz Carlos', 'luiz@email.com', '000@luiz', '(84) 00000-9999', 'ALUNO'),
('111.222.333-44', 'Aísha Marinho', 'marinho.tecnico@uni.edu', '246810@', '(81) 981546328', 'TECNICO'),
('555.666.777-88', 'Maria José', 'maria.tecnica@uni.edu', '13579@', '(81) 991863425', 'TECNICO'),
('999.888.777-66', 'Jailson Calado', 'jailson.tecnico@uni.edu', '36912@', '(87) 981756324', 'TECNICO'),
('987.654.321-01', 'Rhuan Almeida', 'rhuan1@gmail.com', 'Rhuan@23', '(87) 991564872', 'PROFESSOR' ),
('987.654.321-02', 'Kauã Reclione', 'kauare@gmail.com', 'Kauã17@', '(87) 991576252', 'PROFESSOR' ),
('586.496.754-87', 'Jeffeson Sousa', 'jerfferson3n@gmail.com', 'Jeff@769', '(87) 99999-9999', 'ALUNO'),
('579.123.456-85', 'Jorge de Melo', 'jorge07@gmail.com', 'Jorge32@90', '(81) 99256-7881', 'ALUNO'),
('635.478.521-89', 'Maria Helena', 'helena14@gmail.com', 'heLena1417@', '(87) 99264-1665', 'ALUNO'),
('456.821.564-78', 'Levi Ackerman', 'levizin31@gmail.com', 'MTitanM@', '(87) 9918-5882', 'ALUNO'),
('156.256.479-98', 'Edward Elric', 'elric67@gmail.com', 'Alquimia@66', '(87) 98256-6545', 'ALUNO'),
('123.987.456-02', 'Keila Cristina', 'keila01@gmail.com', 'keilinha@02', '(81) 98197-7975', 'ALUNO');

Tabela Aluno
INSERT INTO ALUNO (cpf_aluno, matricula, periodo, id_curso) VALUES ('167.826.000-64', '1400900', 3, 1),
('635.478.521-89', '0022040', 3, 1),
('123.987.456-02', '1099199', 3, 1),
('456.821.564-78', '8008880', 3, 1),
('586.496.754-87', '7077077', 5, 2),
('579.123.456-85', '6066600', 5, 2),
('156.256.479-98', '1102110', 5, 2);

												
Tabela Professor
INSERT INTO PROFESSOR (cpf_professor, titulacao) VALUES 
('180.800.000-12', 'MESTRE'),
('100.200.300-22', 'DOUTOR'),
('987.654.321-01', 'DOUTOR'),
('987.654.321-02', 'DOUTOR');

Tabela Professor Disciplina
INSERT INTO professor_disciplina (id_disciplina, cpf_professor) VALUES 
(1, '222.222.222-22'),
(2, '100.200.300-22'),
(3, '222.222.222-22'),
(4, '100.200.300-22'),
(5, '987.654.321-01'),
(6, '987.654.321-02');

Tabela Professor Especialidade
INSERT INTO PROFESSOR_ESPECIALIDADE (especialidade, cpf_professor) VALUES ('Inteligencia Artificial', '180.800.000-12'),
('Estruturas de Dados', '100.200.300-22'),
('Programação em Python', '987.654.321-01'),
('Programação em Java', '987.654.321-02'),
('Banco de Dados', '222.222.222-22'),
('Engenharia de Software', '222.222.222-22');

Tabela Monitor
INSERT INTO MONITOR (cpf_monitor, turno) VALUES 
('120.001.090-34', 'TARDE'),
('333.333.333-33', 'MANHA');

Tabela Monitor Laboratório
INSERT INTO MONITOR_LABORATORIO (cpf_monitor, id_laboratorio) VALUES ('120.001.090-34', 2),
('333.333.333-33', 1);

Tabela Técnico
INSERT INTO TECNICO (cpf_tecnico, cargo) VALUES 
('700.800.900-01', 'TECNICO_ELETRICO'),
('111.222.333-44', 'TECNICO_TI'),
('555.666.777-88', 'TECNICO_TI'),
('999.888.777-66', 'TECNICO_ELETRICO'),
												
('444.444.444-44', 'TECNICO_TI');

Tabela Técnico Especialidade
INSERT INTO TECNICO_ESPECIALIDADE (especialidade, cpf_tecnico) VALUES ('Manutenção Elétrica', '700.800.900-01'),
('Manutenção de Software', '444.444.444-44'),
('Segurança da Informação', '700.800.900-01'),
('Manutencao de Hardware', '444.444.444-44'),
('Redes e Infraestrutura', '444.444.444-44');

Tabela Curso
INSERT INTO CURSO (nome) VALUES
('licenciatura_em_Computação'),
('Engenharia_de_Software');

Tabela Disciplina
INSERT INTO disciplina (id_disciplina, nome, id_curso) VALUES
(1, 'Banco de Dados', 1),
(2, 'Algoritmos e Estruturas',  1),
(3, 'Engenharia de Requisitos', 2),
(4, 'Qualidade de Software',    2),
(5, 'Programação 1', 1),
(6, 'Programação 2', 2);

Tabela Laboratório
INSERT INTO LABORATORIO (nome, bloco, andar, capacidade, status) VALUES
('Lab de Computação A', 'Bloco A', 1, 30, 'ATIVO'),
('Lab de Computação B', 'Bloco A', 2, 25, 'ATIVO'),
('Lab de Redes', 'Bloco B', 1, 20, 'EM_MANUTENCAO');

Tabela Equipamento
INSERT INTO EQUIPAMENTO (id_equipamento, nome, status, id_laboratorio, id_tipo_equipamento) VALUES 
(1, 'PC-01', 'ATIVO', 1, 1),
(2, 'PC-02', 'ATIVO', 1, 1),
(3, 'PC-03', 'ATIVO', 1, 1),
(4, 'PC-04', 'EM_MANUTENCAO',  1, 1),
(5, 'PC-05', 'ATIVO', 1, 1),
(6, 'Projetor Lab A', 'ATIVO', 1, 2),
(7, 'Switch Lab A',   'ATIVO', 1, 3),
(8, 'PC-06', 'ATIVO', 2, 1),
												
(9, 'PC-07', 'ATIVO', 2, 1),
(10, 'PC-08', 'ATIVO', 2, 1),
(11, 'Projetor Lab B', 'ATIVO', 2, 2),
(12, 'Switch Lab B', 'ATIVO', 2, 3);

Tabela Tipo de Equipamento
INSERT INTO TIPO_EQUIPAMENTO (nome) VALUES
('Computador Desktop'),
('Projetor'),
('Switch de Rede'),
('Impressora');

Tabela Computador
INSERT INTO COMPUTADOR (id_equipamento, sistema_operacional, numero_maquina) VALUES
(1, 'Ubuntu 22.04', 'LAB-A-001'),
(2, 'Ubuntu 22.04', 'LAB-A-002'),
(3, 'Windows 11',   'LAB-A-003'),
(4, 'Windows 11',   'LAB-A-004'),
(5, 'Ubuntu 22.04', 'LAB-A-005'),
(6, 'Windows 11', 'LAB-A-006'),
(7, 'Ubuntu 22.04', 'LAB-B-005'),
(8, 'Windows 11', 'Lab-B-006'),
(9, 'Windows 11', 'Lab-B-007'),
(10, 'Windows 11', 'Lab-B-008'),

Tabela Computador Software
INSERT INTO COMPUTADOR_SOFTWARE (id_software, id_equipamento) VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (1, 2), (2, 2), (4, 2), (1, 3), (4, 3), (5, 3), (4, 4), (1, 5), (2, 5), (3, 5);

Tabela Software
INSERT INTO SOFTWARE (nome, versao, desenvolvedor) VALUES
('VS Code', '1.89',   'Microsoft'),
('Python', '3.12',   'Python Foundation'),
('PostgreSQL', '16.0',   'PostgreSQL Global'),
('Navegador Firefox', '126.0',  'Mozilla'),
('IntelliJ IDEA',  '2024.1', 'JetBrains');

Tabela Reserva
INSERT INTO RESERVA (id_reserva, data_reserva, status, finalidade, id_laboratorio, id_disciplina, cpf_professor) VALUES 
												
('2025-07-10', 'APROVADA', 'Aula pratica de SQL e consultas em banco de dados.', 1, 1, '222.222.222-22'),
(2, '2026-06-20', 'APROVADA', ' Aula pratica de Pilhas e Filas', 2, 2, '100.200.300-22'),
(3, '2026-07-15', 'APROVADA', 'Prova de Banco de Dados.','2026-06-05 21:32', 2, 1, '222.222.222-22'),
(4, '2026-07-20', 'APROVADA', 'Introdução ao Python "hello word".', '2026-06-09 17:29', 1, 5, '987.654.321-01'),
(5, '2026-07-20', 'APROVADA', 'Introdução a Programação Orientada a Objetos.', '2026-06-18 15:16', 2, 6, '987.654.321-02' );

Tabela Horário
INSERT INTO HORARIO (hora_inicio, horario_fim, turno) VALUES
('07:00', '08:40', 'MANHA'),
('08:50', '10:30', 'MANHA'),
('13:00', '14:40', 'TARDE'),
('14:50', '16:30', 'TARDE'),
('19:00', '20:40', 'NOITE'),
('20:50', '22:30', 'NOITE');

Tabela Reserva Horário
INSERT INTO reserva_horario (id_reserva, id_horario) VALUES
(1, 1),
(1, 2),
(3, 3),
(4, 3),
(5, 5);

Tabela Ocorrência
INSERT INTO OCORRENCIA (descricao, prioridade, status, id_laboratorio, id_categoria, cpf_autor) VALUES 
('PC-04 nao liga, possivelmente problema na fonte de alimentacao.', 'ALTA', 'ABERTA', 1, 1, '111.111.111-11'),
('PC-03 com problema no monitor', 'ALTA', 'ABERTA', 2, 1, '167.826.000-64'),
('PC-08 com problema na saida de som', 'ALTA', 'ABERTA', 2, 1, '120.001.090-34'),
('Projetor Lab B nao funciona', 'ALTA', 'ABERTA', 2, 1, '180.800.000-12'),
('PC-01, VS Code esta desatualizado', 'MEDIA', 'ABERTA', 1, 2, '167.826.000-64'),


Tabela Categoria Ocorrência
INSERT INTO CATEGORIA_OCORRENCIA (nome) VALUES
('Equipamento com Defeito'),
												
('Problema de Software'),
('Problema de Rede'),
('Infraestrutura');

Tabela Manutenção
INSERT INTO MANUTENCAO (descricao, tipo_problema, status, id_equipamento, id_laboratorio, id_ocorrencia, cpf_responsavel) VALUES 
('Verificar e consertar Projetor do lab B.', 'HARDWARE', 'ABERTA', 11, 2, 4, '700.800.900-01'),
('Verificar e consertar problema com monitor do PC-03.', 'HARDWARE', 'ABERTA', 3, 1, 2, '700.800.900-01'),
('Verificar e substituir fonte de alimentacao do PC-04.', 'HARDWARE', 'ABERTA', 4, 1, 1, '444.444.444-44');
