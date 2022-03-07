use bagy;

-- Desafio 1 
select StoreId, SUM(Quantity) AS TotaldeItensVendidos, SUM(Quantity * UnitPrice) AS ValorTotal
from dados_ecommerce
group by StoreId
order by ValorTotal desc limit 10;


-- Desafio 2     
select date_format(data, %M) mes, AVG(TotalValue) InvoiceValues 
from 
(select str_to_date(InvoiceDate, %m/%d/%Y) data, 
InvoiceNo, 
SUM(Quantity * UnitPrice) TotalValue 
from dados_ecommerce 
group by data, InvoiceNo) data_trunced 
group by mes 
order by InvoiceValues desc 
    
select date_format(str_to_date(InvoiceDate, %m/%d/%Y), %M) mes, 
AVG(Quantity) media 
from dados_ecommerce 
group by mes 
order by media desc 

select StockCode, sum(quantity) quantity from dados_ecommerce 
where Country = (select Country from dados_ecommerce group by Country order by SUM(Quantity) desc limit 1) 
group by StockCode order by Quantity desc limit 1 
    
select StockCode, sum(quantity) quantity from dados_ecommerce 
where Country = (select Country from dados_ecommerce group by Country order by SUM(Quantity) desc limit 1) 
group by StockCode order by Quantity limit 1 