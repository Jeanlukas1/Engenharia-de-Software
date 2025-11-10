DROP TABLE IF EXISTS cidades CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;
DROP TABLE IF EXISTS pedidos CASCADE;

CREATE TABLE cidades (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100)
);

CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100),
  id_cidade INT REFERENCES cidades(id)
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  descricao VARCHAR(100),
  id_cliente INT REFERENCES clientes(id)
);

INSERT INTO cidades (nome) VALUES
('São Paulo'),
('Rio de Janeiro'),
('Belo Horizonte'),
('Curitiba');

INSERT INTO clientes (nome, id_cidade) VALUES
('Jean Lukas', 1),
('Maria Silva', 2),
('Carlos Andrade', 1),
('Fernanda Souza', 3),
('Bruno Lima', 4),
('Ana Costa', NULL);  -- cliente sem cidade cadastrada

INSERT INTO pedidos (descricao, id_cliente) VALUES
('Compra de Notebook', 1),
('Compra de Smartphone', 1),
('Compra de Cadeira Gamer', 2),
('Compra de Livro', 3),
('Compra de Mesa de Escritório', 3),
('Compra de Headset', 4);


SELECT
	cidades.nome AS Cidade,
	STRING_AGG(clientes.nome, ', ') AS Nome
	
FROM cidades

JOIN clientes ON clientes.id_cidade = clientes.id
GROUP BY cidades.nome;
