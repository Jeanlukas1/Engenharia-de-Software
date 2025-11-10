

DROP TABLE IF EXISTS usuarios CASCADE;
DROP TABLE IF EXISTS livros CASCADE;
DROP TABLE IF EXISTS emprestimos CASCADE;

CREATE TABLE usuarios (
	matricula INT PRIMARY KEY UNIQUE NOT NULL,
	nome VARCHAR(100) UNIQUE NOT NULL,
	curso VARCHAR(100) NOT NULL
);

CREATE TABLE livros (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(255) UNIQUE NOT NULL,
	autor VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE emprestimos (
	id_registro SERIAL PRIMARY KEY,
	titulo_livro VARCHAR(255) REFERENCES livros(titulo),
	autor_livro VARCHAR(100) REFERENCES livros(autor),
	nome_aluno VARCHAR(100) REFERENCES usuarios(nome),
	matricula_aluno INT REFERENCES usuarios(matricula),
	data_emprestimo DATE DEFAULT CURRENT_TIMESTAMP,
	data_devolucao DATE 
);
-- QUESTAO 2
INSERT INTO usuarios(matricula, nome, curso) VALUES
	(2023001, 'Zé da Manga', 'Engenharia'),
	(2023002, 'Zé das Coves', 'Computação'),
	(2023003, 'Goku da Silva', 'Administração'),
	(2023004, 'Titi da Cabral da Silva', 'Ed. Física'),
	(2023005, 'Zé Colmeia', 'Nutrição'),
	(2023006, 'Majin Boo Souza', 'Engenharia de Software'),
	(2023007, 'Gohan das Coves', 'Engenharia de Software'),
	(2023008, 'Cell Oliveira', 'Engenharia de Software'),
	(2023009, 'Jean Lukas de Marins', 'Engenharia de Software');

INSERT INTO livros(titulo, autor) VALUES 
	('A odisseia', 'KungFoo Panda'),
	('Harry Potter', 'J.K. Rowling'),
	('Toy Story', 'Marchall Davis'),
	('As longas tranças de um careca', 'Vegetta'),
	('A vinda dos que não foram', 'Jean Paul');

INSERT INTO emprestimos(titulo_livro, autor_livro, nome_aluno, matricula_aluno, data_devolucao) VALUES
	('A odisseia', 'KungFoo Panda', 'Titi da Cabral da Silva', 2023004, NULL),
	('A vinda dos que não foram', 'Jean Paul', 'Zé Colmeia', 2023005, '2025-09-22'),
	('A odisseia', 'KungFoo Panda', 'Majin Boo Souza', 2023006, '2025-12-11'),
	('Harry Potter', 'J.K. Rowling', 'Gohan das Coves', 2023007, '2025-11-21'),
	('Toy Story', 'Marchall Davis', 'Cell Oliveira', 2023008, '2025-12-12'),
	('As longas tranças de um careca', 'Vegetta', 'Jean Lukas de Marins', 2023009, NULL),
	('A odisseia', 'KungFoo Panda', 'Zé da Manga', 2023001, '2025-11-15'),
	('A odisseia', 'KungFoo Panda', 'Zé das Coves', 2023002, NULL);

-- QUESTAO 3
UPDATE usuarios  SET curso = 'Admnistração' WHERE nome = 'Zé das Coves';
DELETE FROM emprestimos WHERE data_devolucao = CURRENT_TIMESTAMP;


-- QUESTAO 5
SELECT
	usuarios.matricula AS Matricula_Alunos,
	usuarios.nome AS Nome_Alunos,
	usuarios.curso AS Curso_Alunos,
	livros.id AS ID_Livros,
	livros.titulo AS Título_Livros,
	livros.autor AS Autor_Livros,
	emprestimos.id_registro AS Id_Registros_Emprestimos,
	emprestimos.data_emprestimo AS Data_Emprestimos,
	emprestimos.data_devolucao AS Data_Devolucao
FROM
	emprestimos
JOIN
	usuarios ON emprestimos.matricula_aluno = usuarios.matricula
JOIN
	livros ON emprestimos.titulo_livro = livros.titulo;
	


-- -- QUESTAO 5
-- SELECT
-- 	usuarios.matricula AS Matricula_Alunos,
-- 	usuarios.nome AS Nome_Alunos,
-- 	usuarios.curso AS Curso_Alunos,
-- 	livros.id AS ID_Livros,
-- 	livros.titulo AS Título_Livros,
-- 	livros.autor AS Autor_Livros,
-- 	emprestimos.id_registro AS Id_Registros_Emprestimos,
-- 	emprestimos.data_emprestimo AS Data_Emprestimos,
-- 	emprestimos.data_devolucao AS Data_Devolucao
-- FROM
-- 	emprestimos
-- JOIN
-- 	usuarios ON emprestimos.matricula_aluno = usuarios.matricula
-- JOIN
-- 	livros ON emprestimos.titulo_livro = livros.titulo;