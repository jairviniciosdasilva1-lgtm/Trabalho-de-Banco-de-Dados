README.md
# GestLab TI - Sistema de Agendamento de Laboratório de Informática

O **GestLab TI** é um sistema projetado para centralizar a gestão de infraestrutura acadêmica, otimizar o fluxo de reservas de laboratórios e garantir a agilidade no suporte técnico. O projeto engloba desde o levantamento de requisitos e modelagem conceitual até a implementação física de um banco de dados relacional robusto.
Este trabalho foi desenvolvido como requisito para a conclusão da disciplina de **Banco de Dados** do curso de **Licenciatura em Computação** da **Universidade de Pernambuco (UPE)**.


# Escopo do Projeto (Mini-Mundo)

A reitoria e a coordenação de tecnologia da universidade demandaram uma solução integrada para o acompanhamento, reserva e manutenção de seus laboratórios de informática. A partir de reuniões com a Coordenação de Cursos, Equipe de TI e Corpo Docente, foram mapeados os seguintes pilares do sistema:

*   **Controle de Usuários:** Cadastro e gerenciamento de perfis com permissões distintas.
*   **Gestão de Infraestrutura Física:** Cadastro detalhado dos laboratórios disponíveis.
*   **Catálogo de Ativos:** Controle dos equipamentos, computadores e softwares instalados em cada ambiente.
*   **Fluxo de Reservas:** Telas e registros de solicitações vinculadas a horários específicos, cursos e disciplinas.
*   **Suporte Técnico e Ocorrências:** Registro de incidentes por categorias, gerando ordens de serviço automáticas para a equipe de técnicos da instituição.


# Ferramentas Utilizadas

O desenvolvimento do ecossistema do banco de dados seguiu as seguintes etapas e tecnologias:

**Modelagem Conceitual (MER):** [ERDPlus]
**SGBD e Hospedagem do Banco:** [Supabase]
**Ambiente de Desenvolvimento:** [Visual Studio Code (VS Code)]


# Estrutura do Repositório

O projeto está organizado da seguinte forma para facilitar a avaliação e auditoria dos artefatos:


-- Diagramas/          # Modelos conceituais e lógicos (imagens/PDFs do MER)
    -- Diagrama Conceitual
    -- Diagrama Entidade-Relacionamento (ER)
-- Documento Completo/        # Documentação completa do projeto
    -- GestLab TI
-- Roteiros/           # Scripts SQL divididos por função
    -- Criação de Tabelas     
    -- Funções   
    -- GestLab TI #Código completo de aplicação
    -- Povoamento
    -- Triggers
    -- Views
-- README.md          # Este arquivo de apresentação