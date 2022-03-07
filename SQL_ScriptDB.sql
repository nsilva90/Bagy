-- Criação do banco de dados no servidor:
create database bagy;
use bagy;

-- Criação da tabela no banco de dados 'bagy':
create table dados_ecommerce
(
	InvoiceNo 	varchar(100) null, 
	StoreId		varchar(100) null,
	StockCode	varchar(100) null,
	Description	varchar(100) null,
	Quantity	varchar(100) null,
	InvoiceDate varchar(100) null,
	UnitPrice	varchar(100) null,
	CustomerID	varchar(100) null,
	Country		varchar(100) null
);

-- Importação dos dados do arquivo .CSV para a tabela 'dados_ecommerce':
LOAD DATA LOCAL INFILE '/home/nikolas/Bagy/teste_dados_ecommerce.csv'
INTO TABLE dados_ecommerce
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(InvoiceNo, StoreId, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country);

-- Validação da quantidade de registros importados:
select count(*) from dados_ecommerce; -- 541909 registros ok

-- Validação de exibição dos dados:
select * from dados_ecommerce;

------------------------------------------------------------------------------------------------

-- Validação prévia das Querys no SQL Workbench antes de implementá-las no código Python:

-- use bagy;

-- Desafio 1 
-- SELECT StoreId, SUM(Quantity) AS TotaldeItensVendidos, SUM(Quantity * UnitPrice) AS ValorTotal
-- FROM dados_ecommerce
-- GROUP BY StoreId
-- ORDER BY ValorTotal DESC LIMIT 10;

-- Desafio 2.1     
-- SELECT date_format(data, '%M') AS Mes, AVG(ValorTotal) AS TicketMedioDosPedidos
-- FROM
-- 	(SELECT str_to_date(InvoiceDate, '%m/%d/%Y') AS data,
-- 	InvoiceNo,
-- 	SUM(Quantity * UnitPrice) AS ValorTotal
-- 	FROM dados_ecommerce
-- 	GROUP BY data, InvoiceNo) AS date
-- GROUP BY Mes
-- ORDER BY TicketMedioDosPedidos desc;

-- Desafio 2.2  
-- SELECT date_format(data, '%M') AS Mes,
-- AVG(NumeroDePedidos) AS MediaDePedidos
-- FROM
-- 	(SELECT str_to_date(InvoiceDate, '%m/%d/%Y') AS data,
-- 	StoreId,
-- 	COUNT(InvoiceNo) AS NumeroDePedidos
-- 	FROM dados_ecommerce
-- 	GROUP BY data, StoreId) AS date
-- GROUP BY Mes
-- ORDER BY MediaDePedidos DESC;

-- Desafio 3.1  
-- SELECT Country, Description, sum(quantity) AS QuantidadeTotal FROM dados_ecommerce 
-- WHERE Country = 
-- 	(SELECT Country 
-- 	FROM dados_ecommerce 
-- 	GROUP BY Country 
-- 	ORDER BY SUM(Quantity) DESC 
-- 	LIMIT 1) 
-- GROUP BY Description, Country 
-- ORDER BY QuantidadeTotal DESC LIMIT 1;

-- Desafio 3.2    
-- SELECT Country, Description, sum(quantity) AS QuantidadeTotal FROM dados_ecommerce 
-- WHERE Country = 
-- 	(SELECT Country 
-- 	FROM dados_ecommerce 
-- 	GROUP BY Country 
-- 	ORDER BY SUM(Quantity) DESC 
-- 	LIMIT 1) 
-- GROUP BY Description, Country 
-- ORDER BY QuantidadeTotal LIMIT 1;