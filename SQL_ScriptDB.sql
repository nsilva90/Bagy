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




