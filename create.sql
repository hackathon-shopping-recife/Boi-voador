-- Schema: public
DROP TABLE backend_item;

DROP TABLE backend_cliente;

DROP TABLE backend_compra;

CREATE TABLE "backend_cliente" (
	"id" serial NOT NULL PRIMARY KEY,
    "cpf"		varchar (11)  NOT NULL,
	"senha"		varchar (30) NOT NULL,
	"endereco"	varchar (50) NOT NULL,
	"telefone"	varchar (20) NOT NULL,
	"email"		varchar (30) NOT NULL,
	"id_comprador"	integer  NOT NULL
);

CREATE TABLE "backend_compra" (
	"id" serial NOT NULL PRIMARY KEY,
	"id_comprador"	integer NOT NULL,
	"cnpj" 			varchar (20) NOT NULL,
	"valor"			decimal NOT NULL,
	"qnt_itens"		integer NOT NULL,
	"url"			varchar(200) NOT NULL UNIQUE,
	"data_emissao" 	varchar(30) NOT NULL
);

CREATE TABLE "backend_item" (
	"id" serial NOT NULL PRIMARY KEY,
	"descricao" 	varchar(30) NOT NULL,
	"valor"			decimal NOT NULL,
	"compra_id"		integer NOT NULL
);

CREATE INDEX "backend_cliente_cpf_f1b0aa00_like" ON "backend_cliente" ("cpf" varchar_pattern_ops);
CREATE INDEX "backend_compra_url_9ddb015e_like" ON "backend_compra" ("url" varchar_pattern_ops);

-- INSERT INTO backend_cliente (cpf,senha,endereco,telefone,email,id_comprador)
-- 	VALUES ('09798299418', '123456', 'Rua dos Poucos,nº 0', '21011111', 'artuzinho@teste.com', 1);


-- INSERT INTO backend_cliente (cpf,senha,endereco,telefone,email,id_comprador)
-- 	VALUES ('10181593475', '123456', 'Rua da Alfandega,nº 1', '35051012', 'douglinhas@teste.com', 2);

	
-- INSERT INTO backend_cliente (cpf,senha,endereco,telefone,email,id_comprador)
-- 	VALUES ('23454367898', '123456', 'Rua do Cais,nº 2', '23456789', 'lukinhas@teste.com', 3);

	
-- INSERT INTO backend_cliente (cpf,senha,endereco,telefone,email,id_comprador)
-- 	VALUES ('64628989850', '123456', 'Rua do Apolo,nº 3', '08000800', 'ramones@teste.com', 4);
	
	
-- INSERT INTO backend_cliente (cpf,senha,endereco,telefone,email,id_comprador)
-- 	VALUES ('98756754467', '123456', 'Rua do Sertão,nº 4', '35051012', 'bekenballwer@teste.com', 5);


-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao, url)
-- 	VALUES (1,1,'05.402.939/0001-04',60,1,'28/09/2018 11:55:44', 'bla');


-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao, url)
-- 	VALUES (2,1,'03.403.939/0005-09',55,1,'23/09/2018 12:13:45', 'aaida');
	
-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao, url)
-- 	VALUES (3,2,'02.401.939/0004-08',320,1,'15/09/2018 09:43:46', 'aopsaod');

-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao)
-- 	VALUES (4,2,'07.402.939/0003-05',80.99,1,'10/09/2018 18:22:47');


-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao)
-- 	VALUES (5,3,'06.404.939/0002-04',400,1,'30/09/2018 19:25:48');


-- INSERT INTO backend_compra (id_compra,id_comprador,cnpj,valor,qnt_itens,data_emissao)
-- 	VALUES (6,4,'05.405.939/0001-01',450.99,1,'28/09/2018 21:03:39');
