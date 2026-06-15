Criação de Tabelas
CREATE TYPE tipo_usuario_enum   AS ENUM ('ALUNO', 'PROFESSOR', 'MONITOR', 'TECNICO');
CREATE TYPE turno_enum          AS ENUM ('MANHA', 'TARDE', 'NOITE');
CREATE TYPE status_lab_enum     AS ENUM ('ATIVO', 'INATIVO', 'EM_MANUTENCAO');
CREATE TYPE status_equip_enum   AS ENUM ('ATIVO', 'INATIVO', 'EM_MANUTENCAO');
CREATE TYPE status_reserva_enum AS ENUM ('PENDENTE', 'APROVADA', 'CANCELADA', 'CONCLUIDA');
CREATE TYPE prioridade_enum     AS ENUM ('BAIXA', 'MEDIA', 'ALTA', 'CRITICA');
CREATE TYPE status_ocorr_enum   AS ENUM ('ABERTA', 'EM_ANDAMENTO', 'RESOLVIDA', 'FECHADA');
CREATE TYPE status_manut_enum   AS ENUM ('ABERTA', 'EM_ANDAMENTO', 'CONCLUIDA', 'CANCELADA');
CREATE TYPE cargo_enum AS ENUM ( 'TECNICO_TI', 'TECNICO_ELETRICO', 'TECNICO_REDES', 'TECNICO_SUPORTE', 'OUTRO');
CREATE TYPE tipo_problema_enum AS ENUM ('HARDWARE', 'SOFTWARE', 'REDE', 'ENERGIA', 'OUTRO');
CREATE TYPE titulacao_enum AS ENUM ('GRADUADO', 'ESPECIALISTA', 'MESTRE', 'DOUTOR', 'POS_DOUTOR');


CREATE TABLE CURSO (
    id_curso SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE USUARIO (
    CPF CHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    tipo_usuario tipo_usuario_enum NOT NULL
);


CREATE TABLE ALUNO (
    cpf_aluno CHAR(14) PRIMARY KEY REFERENCES USUARIO (CPF),
    matricula VARCHAR(20) NOT NULL UNIQUE,
    periodo SMALLINT NOT NULL,
    id_curso INT NOT NULL REFERENCES CURSO (id_curso)
);


CREATE TABLE PROFESSOR (
    cpf_professor CHAR(14) PRIMARY KEY REFERENCES USUARIO (CPF),
    titulacao titulacao_enum NOT NULL
);


CREATE TABLE PROFESSOR_ESPECIALIDADE (
    especialidade VARCHAR(100) NOT NULL,
    cpf_professor CHAR(14) NOT NULL REFERENCES PROFESSOR (cpf_professor),
    PRIMARY KEY (especialidade, cpf_professor)
);


CREATE TABLE TECNICO (
    cpf_tecnico CHAR(14) PRIMARY KEY REFERENCES USUARIO (CPF),
    cargo cargo_enum NOT NULL
);


CREATE TABLE TECNICO_ESPECIALIDADE (
    especialidade VARCHAR(100) NOT NULL,
    cpf_tecnico CHAR(14) NOT NULL REFERENCES TECNICO (cpf_tecnico),
    PRIMARY KEY (especialidade, cpf_tecnico)
);


CREATE TABLE MONITOR (
    cpf_monitor CHAR(14) PRIMARY KEY REFERENCES USUARIO (CPF),
    turno turno_enum NOT NULL
);


CREATE TABLE DISCIPLINA (
    id_disciplina SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_curso INT NOT NULL REFERENCES CURSO (id_curso)
);


CREATE TABLE PROFESSOR_DISCIPLINA (
    id_disciplina INT NOT NULL REFERENCES DISCIPLINA (id_disciplina),
    cpf_professor CHAR(14) NOT NULL REFERENCES PROFESSOR (cpf_professor),
    PRIMARY KEY (id_disciplina, cpf_professor)
);


CREATE TABLE HORARIO (
    id_horario SERIAL PRIMARY KEY,
    hora_inicio TIME NOT NULL,
    horario_fim TIME NOT NULL,
    turno turno_enum NOT NULL
);


CREATE TABLE LABORATORIO (
    id_laboratorio SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    bloco VARCHAR(20) NOT NULL,
    andar SMALLINT NOT NULL,
    capacidade SMALLINT NOT NULL,
    status status_lab_enum NOT NULL DEFAULT 'ATIVO'
);


CREATE TABLE MONITOR_LABORATORIO (
    cpf_monitor CHAR(14) NOT NULL REFERENCES MONITOR (cpf_monitor),
    id_laboratorio INT NOT NULL REFERENCES LABORATORIO (id_laboratorio),
    PRIMARY KEY (cpf_monitor, id_laboratorio)
);


CREATE TABLE TIPO_EQUIPAMENTO (
    id_tipo_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
);


CREATE TABLE EQUIPAMENTO (
    id_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    status status_equip_enum NOT NULL DEFAULT 'ATIVO',
    id_laboratorio INT NOT NULL REFERENCES LABORATORIO (id_laboratorio),
    id_tipo_equipamento INT NOT NULL REFERENCES TIPO_EQUIPAMENTO (id_tipo_equipamento)
);


CREATE TABLE SOFTWARE (
    id_software SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    versao VARCHAR(30)  NOT NULL,
    desenvolvedor VARCHAR(100) NOT NULL,
    UNIQUE (nome, versao)
);


CREATE TABLE COMPUTADOR (
    id_equipamento INT PRIMARY KEY REFERENCES EQUIPAMENTO (id_equipamento),
    sistema_operacional VARCHAR(80) NOT NULL,
    numero_maquina VARCHAR(30) NOT NULL UNIQUE
);


CREATE TABLE COMPUTADOR_SOFTWARE (
    id_software INT NOT NULL REFERENCES SOFTWARE (id_software),
    id_equipamento INT NOT NULL REFERENCES COMPUTADOR (id_equipamento),
    PRIMARY KEY (id_software, id_equipamento)
);


CREATE TABLE RESERVA (
    id_reserva SERIAL PRIMARY KEY,
    data_reserva DATE NOT NULL,
    status status_reserva_enum NOT NULL DEFAULT 'PENDENTE',
    finalidade VARCHAR(255) NOT NULL,
    data_solicitacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_laboratorio INT NOT NULL REFERENCES LABORATORIO (id_laboratorio),
    id_disciplina INT REFERENCES DISCIPLINA (id_disciplina),
    cpf_professor CHAR(14) REFERENCES PROFESSOR  (cpf_professor)
);


CREATE TABLE RESERVA_HORARIO (
    id_reserva INT NOT NULL REFERENCES RESERVA (id_reserva),
    id_horario INT NOT NULL REFERENCES HORARIO (id_horario),
    PRIMARY KEY (id_reserva, id_horario)
);


CREATE TABLE CATEGORIA_OCORRENCIA (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(80)  NOT NULL UNIQUE
);


CREATE TABLE OCORRENCIA (
    id_ocorrencia SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
    prioridade prioridade_enum NOT NULL DEFAULT 'MEDIA',
    status status_ocorr_enum NOT NULL DEFAULT 'ABERTA',
    data_ocorrencia TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_laboratorio INT NOT NULL REFERENCES LABORATORIO (id_laboratorio),
    id_categoria INT NOT NULL REFERENCES CATEGORIA_OCORRENCIA (id_categoria),
    cpf_autor CHAR(14) NOT NULL REFERENCES USUARIO (CPF)
);


CREATE TABLE MANUTENCAO (
    id_manutencao SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
    tipo_problema tipo_problema_enum NOT NULL,
    status status_manut_enum NOT NULL DEFAULT 'ABERTA',
    data_abertura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_conclusao TIMESTAMP,
    id_equipamento INT NOT NULL REFERENCES EQUIPAMENTO (id_equipamento),
    id_laboratorio INT NOT NULL REFERENCES LABORATORIO (id_laboratorio),
    id_ocorrencia INT REFERENCES OCORRENCIA  (id_ocorrencia),
    cpf_responsavel CHAR(14) NOT NULL REFERENCES TECNICO     (cpf_tecnico)
);