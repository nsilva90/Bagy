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

# Desafio 1

print("1) Quais as 10 lojas com maior faturamento em pedidos? Sumarize os dados dessa loja apresentando os seguintes campos:\n"
"- StoreId\n"
"- Volume total de itens vendidos\n"
"- Valor total vendido\n"
"\n"
"Resposta:")

cursor.execute(
    'select StoreId, SUM(Quantity) Quantity, SUM(UnitPrice) Billing '
    'from dados_ecommerce '
    'group by StoreId '
    'order by sum(UnitPrice) desc limit 10 '
)

for line in cursor.fetchall():
    print(f"StoreId: {line[0]}, Volume total de itens vendidos: {line[1]}, Valor total vendido: {line[2]}")


# Desafio 2

print("\n"
"--------------------------------------------------------------------------------------------\n"
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
    print(f"Mês: {line[0]}, Média de Valor dos Pedidos: {line[1]}")

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
    print(f"Mês: {line[0]}, Média de vendas: {line[1]}")








