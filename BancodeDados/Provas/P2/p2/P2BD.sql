
-- ============================ 
-- TABELA DEPARTAMENTOS 
-- ============================ 
CREATE TABLE departamentos ( 
    id_departamento SERIAL PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL 
); 
 
-- ============================ 
-- TABELA FUNCIONARIOS 
-- ============================ 
CREATE TABLE funcionarios ( 
    id_funcionario SERIAL PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    cargo VARCHAR(255) NOT NULL, 
    salario NUMERIC(10,2) NOT NULL, 
    id_departamento INT NOT NULL REFERENCES departamentos(id_departamento) 
); 
 
-- ============================ 
-- TABELA PROJETOS 
-- ============================ 
CREATE TABLE projetos ( 
    id_projeto SERIAL PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    descricao TEXT, 
    id_departamento INT NOT NULL REFERENCES departamentos(id_departamento) 
); 
 
-- ============================ 
-- TABELA DE LOGS DE PROJETOS 
-- ============================ 
CREATE TABLE log_projetos ( 
    id_log SERIAL PRIMARY KEY, 
    id_projeto INT NOT NULL, 
    operacao VARCHAR(50) NOT NULL, 
    data_operacao TIMESTAMP NOT NULL 
); 

CREATE OR REPLACE FUNCTION trigger_projeto() 
RETURNS TRIGGER AS $$ 
BEGIN
	INSERT INTO log_projetos(id_projeto, operacao, data_operacao) VALUES 
		(NEW.id_projeto, 'INSERT', CURRENT_TIMESTAMP); 
	
	RETURN NEW; 

END; 
$$ LANGUAGE plpgsql; 
 
CREATE TRIGGER projeto_trigger 
AFTER INSERT ON projetos 
FOR EACH ROW 
EXECUTE FUNCTION trigger_projeto();


CREATE VIEW vw_funcionario_projetos AS
SELECT
    f.nome AS nome_funcionario,
    f.cargo,
    d.nome AS nome_departamento,
    p.nome AS nome_projeto,
    p.descricao
FROM funcionarios f
JOIN departamentos d ON f.id_departamento = d.id_departamento
JOIN projetos p ON p.id_departamento = d.id_departamento
ORDER BY f.nome;


CREATE USER usuario_read_Jean WITH PASSWORD 'jean';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO usuario_read_Jean;

INSERT INTO departamentos (nome) VALUES 
    ('Escola');

INSERT INTO funcionarios (nome, cargo, salario, id_departamento) VALUES 
	('Jean', 'Eng. de Software', 1000, 1);

INSERT INTO projetos (nome, descricao, id_departamento) VALUES 
	('Software de biblioteca', 'Criar um software de gerenciamento de biblioteca', 1);
SELECT * FROM departamentos;
