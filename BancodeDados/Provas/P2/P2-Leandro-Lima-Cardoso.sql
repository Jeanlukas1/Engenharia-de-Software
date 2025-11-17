-- 1. Criação do Banco de Dados:
CREATE TABLE medico (
	id_medico SERIAL PRIMARY KEY,
	especialidade VARCHAR(100) NOT NULL,
	nome VARCHAR(100) NOT NULL
);

CREATE TABLE paciente (
	id_paciente SERIAL PRIMARY KEY,
	data_nascimento DATE NOT NULL,
	nome VARCHAR(100) NOT NULL
);

CREATE TABLE consulta (
	id_consulta SERIAL PRIMARY KEY,
	data_consulta TIMESTAMP NOT NULL,
	id_medico INT NOT NULL,
	id_paciente INT NOT NULL,
	valor NUMERIC(10, 2) NOT NULL,
	FOREIGN KEY (id_medico) REFERENCES medico(id_medico),
	FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente)
);

CREATE TABLE log_consulta (
	id_log SERIAL PRIMARY KEY,
	data_hora_log TIMESTAMP,
	id_consulta INT NOT NULL,
	FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);

-- 2. Crie uma VIEW:
CREATE OR REPLACE VIEW main_view AS
SELECT
	medico.nome AS nome_medico,
	paciente.nome AS nome_paciente,
	consulta.data_consulta,
	consulta.valor
FROM
	consulta
JOIN
	medico ON medico.id_medico = consulta.id_consulta
JOIN
	paciente ON paciente.id_paciente = consulta.id_consulta;

-- 3. Trigger de log_consulta:
CREATE OR REPLACE FUNCTION func_log()
RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO log_consulta (id_consulta) VALUES 
		(NEW.id_consulta);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_trigger
AFTER INSERT ON consulta
FOR EACH ROW
EXECUTE FUNCTION func_log();

-- 4. Criação de usuário com permissões específicas:
CREATE USER luna WITH PASSWORD 'leandro';
GRANT ALL ON ALL TABLES IN SCHEMA public TO leandro;
