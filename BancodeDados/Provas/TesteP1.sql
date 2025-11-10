
-- Criação das tabelas

CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);

CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150),
    autor_id INT REFERENCES autores(id),
    genero VARCHAR(50)
);

CREATE TABLE emprestimos (
    id SERIAL PRIMARY KEY,
    livro_id INT REFERENCES livros(id),
    data_emprestimo DATE,
    data_devolucao DATE
);

-- Inserção de coluna
ALTER TABLE livros ADD COLUMN ano_publicacao INT;

-- Remoção de coluna
ALTER TABLE livros DROP COLUMN ano_publicacao;

-- Backup de tabela com condição WHERE
CREATE TABLE livros_modernos AS
SELECT * FROM livros
WHERE genero = 'Ficção';

-- INNER JOIN
SELECT livros.titulo, autores.nome
FROM livros
INNER JOIN autores ON livros.autor_id = autores.id;

-- FULL JOIN
SELECT livros.titulo, autores.nome
FROM livros
FULL JOIN autores ON livros.autor_id = autores.id;

-- CROSS JOIN
SELECT livros.titulo, autores.nome
FROM livros
CROSS JOIN autores;

-- Inserção de dados aleatórios

-- Autores
INSERT INTO autores (nome, nacionalidade)
SELECT
    LEFT(md5(random()::text), 10),
    CASE WHEN random() > 0.5 THEN 'Brasil' ELSE 'Portugal' END
FROM generate_series(1, 20);

-- Livros
INSERT INTO livros (titulo, autor_id, genero)
SELECT
    LEFT(md5(random()::text), 15),
    (SELECT id FROM autores ORDER BY random() LIMIT 1),
    CASE WHEN random() > 0.5 THEN 'Ficção' ELSE 'História' END
FROM generate_series(1, 50);

-- Empréstimos
INSERT INTO emprestimos (livro_id, data_emprestimo, data_devolucao)
SELECT
    id,
    current_date - (random() * 365)::int,
    current_date + (random() * 30)::int
FROM livros
ORDER BY random()
LIMIT 30;
