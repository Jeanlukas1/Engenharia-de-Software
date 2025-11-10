CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL CHECK (idade > 0),
    curso VARCHAR(100) NOT NULL
);

CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    disciplina VARCHAR(100) NOT NULL
);

INSERT INTO alunos (nome, idade, curso) VALUES
	('Jean Lukas de Marins Costa do Nascimento', 20, 'Eng software');

INSERT INTO professores (nome, disciplina) VALUES
	('Zé da Manga', 'Eng software');

DELETE FROM alunos WHERE id = 1;

UPDATE alunos SET nome = 'Zé das coves' WHERE id = 1;

SELECT * FROM professores;
