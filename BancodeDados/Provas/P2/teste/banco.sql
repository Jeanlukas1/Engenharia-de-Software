

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    tipo VARCHAR(20) CHECK (tipo IN ('aluno', 'funcionario')) NOT NULL,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    ano_publicacao INT,
    disponivel BOOLEAN DEFAULT TRUE
);

CREATE TABLE emprestimos (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    livro_id INT NOT NULL REFERENCES livros(id) ON DELETE CASCADE,
    data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_real DATE,
    status VARCHAR(20) DEFAULT 'em_andamento' CHECK (status IN ('em_andamento', 'devolvido'))
);

INSERT INTO usuarios (nome, email, tipo) VALUES
('Jean Lukas de Marins Costa','lukasjean@gmail.com','aluno'),
('ze das coves', 'ze@email.com', 'aluno'),
('goku da silva', 'goku@email.com', 'aluno'),
('Vegetta', 'vegetta@email.com', 'funcionario'),
('Gohan', 'gohan@email.com', 'aluno');

INSERT INTO livros (titulo, autor, isbn, ano_publicacao) VALUES
('Harry Potter', 'J.K.Rowling', '978-85-359-0277-5', 1899),
('O açogueiro', 'André', '978-85-359-0278-2', 1890),
('Mimico', 'Joao sa', '978-85-359-0279-9', 1881),
('Iracema', 'José de Alencar', '978-85-359-0280-5', 1865),
('O Guarani', 'José de Alencar', '978-85-359-0281-2', 1857);

INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo, data_devolucao_prevista, status) VALUES
(1, 1, '2024-01-15', '2024-02-15', 'em_andamento'),
(2, 2, '2024-01-20', '2024-02-20', 'em_andamento'),
(1, 3, '2023-12-01', '2024-01-01', 'devolvido'),
(3, 4, '2024-01-10', '2024-02-10', 'em_andamento');

UPDATE livros SET disponivel = FALSE WHERE id IN (1, 2, 4);

CREATE TABLE log_emprestimos (
    id SERIAL PRIMARY KEY,
    operacao VARCHAR(10) NOT NULL CHECK (operacao IN ('INSERT', 'UPDATE', 'DELETE')),
    emprestimo_id INT NOT NULL,
    usuario_responsavel VARCHAR(100),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dados_antigos JSONB,
    dados_novos JSONB
);

CREATE OR REPLACE FUNCTION log_emprestimos_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO log_emprestimos (operacao, emprestimo_id, dados_novos)
        VALUES ('INSERT', NEW.id, row_to_json(NEW));
        RETURN NEW;
    END IF;
    
    IF TG_OP = 'UPDATE' THEN
        INSERT INTO log_emprestimos (operacao, emprestimo_id, dados_antigos, dados_novos)
        VALUES ('UPDATE', NEW.id, row_to_json(OLD), row_to_json(NEW));
        RETURN NEW;
    END IF;
    
    IF TG_OP = 'DELETE' THEN
        INSERT INTO log_emprestimos (operacao, emprestimo_id, dados_antigos)
        VALUES ('DELETE', OLD.id, row_to_json(OLD));
        RETURN OLD;
    END IF;
    
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_log_emprestimos
    AFTER INSERT OR UPDATE OR DELETE ON emprestimos
    FOR EACH ROW
    EXECUTE FUNCTION log_emprestimos_trigger();

CREATE VIEW view_emprestimos_completa AS
SELECT 
    e.id AS emprestimo_id,
    u.nome AS nome_usuario,
    u.email AS email_usuario,
    u.tipo AS tipo_usuario,
    l.titulo AS titulo_livro,
    l.autor AS autor_livro,
    l.isbn AS isbn_livro,
    e.data_emprestimo,
    e.data_devolucao_prevista,
    e.data_devolucao_real,
    e.status,
    CASE 
        WHEN e.data_devolucao_real IS NOT NULL THEN 'Devolvido'
        WHEN e.data_devolucao_prevista < CURRENT_DATE THEN 'Atrasado'
        ELSE 'Em andamento'
    END AS status_descritivo,
    CASE 
        WHEN e.data_devolucao_real IS NOT NULL THEN 
            e.data_devolucao_real - e.data_emprestimo
        ELSE 
            CURRENT_DATE - e.data_emprestimo
    END AS dias_emprestado
FROM emprestimos e
INNER JOIN usuarios u ON e.usuario_id = u.id
INNER JOIN livros l ON e.livro_id = l.id
ORDER BY e.data_emprestimo DESC;

CREATE USER biblioteca_admin WITH PASSWORD 'admin123';

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO biblioteca_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO biblioteca_admin;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO biblioteca_admin;

ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT ALL PRIVILEGES ON TABLES TO biblioteca_admin;

CREATE USER biblioteca_leitor WITH PASSWORD 'leitor123';

GRANT SELECT ON view_emprestimos_completa TO biblioteca_leitor;

SELECT * FROM view_emprestimos_completa;

SELECT * FROM view_emprestimos_completa WHERE status = 'em_andamento';

SELECT * FROM view_emprestimos_completa WHERE status_descritivo = 'Atrasado';

SELECT nome_usuario, COUNT(*) as total_emprestimos
FROM view_emprestimos_completa
GROUP BY nome_usuario
ORDER BY total_emprestimos DESC;

SELECT * FROM log_emprestimos ORDER BY data_hora DESC;

INSERT INTO emprestimos (usuario_id, livro_id, data_devolucao_prevista)
VALUES (4, 5, '2024-03-01');

SELECT * FROM log_emprestimos WHERE operacao = 'INSERT' ORDER BY id DESC LIMIT 1;

UPDATE emprestimos 
SET status = 'devolvido', data_devolucao_real = CURRENT_DATE 
WHERE id = 1;

SELECT * FROM log_emprestimos WHERE operacao = 'UPDATE' ORDER BY id DESC LIMIT 1;



SELECT trigger_name, event_manipulation, event_object_table
FROM information_schema.triggers
WHERE event_object_table = 'emprestimos';

SELECT grantee, privilege_type, table_name
FROM information_schema.role_table_grants
WHERE grantee = 'biblioteca_leitor';

CREATE OR REPLACE VIEW view_logs_completa AS
SELECT 
    l.id,
    l.operacao,
    l.emprestimo_id,
    l.usuario_responsavel,
    l.data_hora,
    e.livro_id,
    e.usuario_id,
    l.dados_antigos,
    l.dados_novos,
    CASE 
        WHEN l.operacao = 'INSERT' THEN 'Inserção'
        WHEN l.operacao = 'UPDATE' THEN 'Atualização'
        WHEN l.operacao = 'DELETE' THEN 'Exclusão'
        ELSE l.operacao
    END AS operacao_descritiva
FROM log_emprestimos l
LEFT JOIN emprestimos e ON l.emprestimo_id = e.id
ORDER BY l.data_hora DESC;


