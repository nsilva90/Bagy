from datetime import datetime
from sqlite3 import Cursor
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    user="nikolas",
    password="lenovo29",
    database="bagy"
)

cursor = conn.cursor()

# ----------------------------------------------------------------------------------------------------

# Desafio 1

print("1) Quais as 10 lojas com maior faturamento em pedidos? Sumarize os dados dessa loja apresentando os seguintes campos:\n"
"- StoreId\n"
"- Volume total de itens vendidos\n"
"- Valor total vendido\n"
"\n"
"Resposta:")

cursor.execute(
    "select StoreId, SUM(Quantity) AS TotaldeItensVendidos, SUM(Quantity * UnitPrice) AS ValorTotal "
    "from dados_ecommerce "
    "group by StoreId "
    "order by ValorTotal desc limit 10 "
)

for line in cursor.fetchall():
    print(f"StoreId: {line[0]}, Volume total de itens vendidos: {round(line[1], 0)}, Valor total vendido: $ {round(line[2], 2)}")

# ----------------------------------------------------------------------------------------------------

# Desafio 2

print("\n"
"\n"
"2.1) Qual ticket médio mensal dos pedidos apresentados?\n"
"\n"
"Resposta:")

cursor.execute(
    "select date_format(data, '%M') mes, AVG(TotalValue) InvoiceValues "
    "from "
    "(select str_to_date(InvoiceDate, '%m/%d/%Y') data, "
    "InvoiceNo, "
    "SUM(Quantity * UnitPrice) TotalValue "
    "from dados_ecommerce "
    "group by data, InvoiceNo) data_trunced "
    "group by mes "
    "order by InvoiceValues desc "
)

for line in cursor.fetchall():
    print(f"Mês: {line[0]}, Média de Valor dos Pedidos: $ {round(line[1], 2)}")

print("\n"
"2.2) Qual o volume médio mensal de vendas (todas as lojas)?\n"
"\n"
"Resposta:")

cursor.execute(
    "select date_format(str_to_date(InvoiceDate, '%m/%d/%Y'), '%M') mes, "
    "AVG(Quantity) media "
    "from dados_ecommerce "
    "group by mes "
    "order by media desc "
)

for line in cursor.fetchall():
    print(f"Mês: {line[0]}, Média de vendas: {round(line[1], 0)}")

# ----------------------------------------------------------------------------------------------------

# Desafio 3

print("\n"
"\n"
"3.1) Qual o item mais vendido no país com maior volume de vendas?\n"
"\n"
"Resposta:")

cursor.execute(
    # "select Country, SUM(Quantity) VolumeTotal from dados_ecommerce "
    # "group by Country "
    "select StockCode, sum(quantity) quantity from dados_ecommerce "
    "where Country = (select Country from dados_ecommerce group by Country order by SUM(Quantity) desc limit 1) "
    "group by StockCode order by Quantity desc limit 1 "
)

for line in cursor.fetchall():
    print(f"O item mais vendido foi: {line[0]}, com {line[1]} unidades vendidas")

print("\n"
"3.2) Qual o item menos vendido no país com maior volume de vendas?\n"
"\n"
"Resposta:")

cursor.execute(
    # "select Country, SUM(Quantity) VolumeTotal from dados_ecommerce "
    # "group by Country "
    "select StockCode, sum(quantity) quantity from dados_ecommerce "
    "where Country = (select Country from dados_ecommerce group by Country order by SUM(Quantity) desc limit 1) "
    "group by StockCode order by Quantity limit 1 "
)

for line in cursor.fetchall():
    print(f"O item menos vendido foi: {line[0]}, com {line[1]} unidades vendidas")