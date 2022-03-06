create database bagy;
use bagy;

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

select * from dados_ecommerce;