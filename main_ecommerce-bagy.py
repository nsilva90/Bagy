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

# O 'cursor execute' envia as 'querys' para o servidor SQL e armazena os dados retornados:
cursor.execute(
    "SELECT StoreId, SUM(Quantity) AS TotaldeItensVendidos, SUM(Quantity * UnitPrice) AS ValorTotal "
    "FROM dados_ecommerce "
    "GROUP BY StoreId "
    "ORDER BY ValorTotal DESC LIMIT 10 "
)

# Através de um loop, o 'cursor fetchall' busca cada um dos registros armazenados como tuplas no cursor e os apresenta em forma de lista:
for line in cursor.fetchall():
    print(f"StoreId: {line[0]}, Volume total de itens vendidos: {round(line[1], 0)}, Valor total vendido: $ {round(line[2], 2)}")

# ----------------------------------------------------------------------------------------------------

# Desafio 2

print("\n"
"\n"
"2.1) Qual ticket médio mensal dos pedidos apresentados?\n"
"\n"
"Resposta:\n")

# O 'cursor execute' envia as 'querys' para o servidor SQL e armazena os dados retornados:
cursor.execute(
    "SELECT date_format(data, '%M') AS Mes, AVG(ValorTotal) AS TicketMedioDosPedidos "
    "FROM "
        "(SELECT str_to_date(InvoiceDate, '%m/%d/%Y') AS data, "
        "InvoiceNo, "
        "SUM(Quantity * UnitPrice) AS ValorTotal "
        "FROM dados_ecommerce "
        "GROUP BY data, InvoiceNo) AS date "
    "GROUP BY Mes "
    "ORDER BY TicketMedioDosPedidos desc "
)

print(f"- Os resultados estão ordenados em ordem decrescente, do mês com maior ticket médio para o menor:\n")
# Através de um loop, o 'cursor fetchall' busca cada um dos registros armazenados como tuplas no cursor e os apresenta em forma de lista:
for line in cursor.fetchall():
    print(f"Mês: {line[0]} - Ticket médio dos pedidos: $ {round(line[1], 2)}")

print("\n"
"2.2) Qual o volume médio mensal de vendas (todas as lojas)?\n"
"\n"
"Resposta:\n")

# O 'cursor execute' envia as 'querys' para o servidor SQL e armazena os dados retornados: 
cursor.execute(
"SELECT date_format(data, '%M') AS Mes, AVG(NumeroDePedidos) AS MediaDePedidos "
"FROM "
	"(SELECT str_to_date(InvoiceDate, '%m/%d/%Y') AS data, "
	"StoreId, "
	"COUNT(InvoiceNo) AS NumeroDePedidos "
	"FROM dados_ecommerce "
	"GROUP BY data, StoreId) AS date "
"GROUP BY Mes "
"ORDER BY MediaDePedidos DESC "
)

print(f"- Os resultados estão ordenados em ordem decrescente, do mês com a maior média de vendas para o menor:\n")
# Através de um loop, o 'cursor fetchall' busca cada um dos registros armazenados como tuplas no cursor e os apresenta em forma de lista:
for line in cursor.fetchall():
    print(f"Mês: {line[0]}, Média de vendas: {round(line[1], 0)}")

# ----------------------------------------------------------------------------------------------------

# Desafio 3

print("\n"
"\n"
"3.1) Qual o item mais vendido no país com maior volume de vendas?\n"
"\n"
"Resposta:\n")

cursor.execute(
    "SELECT Country, Description, sum(quantity) AS QuantidadeTotal FROM dados_ecommerce "
    "WHERE Country = "
        "(SELECT Country FROM dados_ecommerce "
        "GROUP BY Country "
        "ORDER BY SUM(Quantity) DESC "
        "LIMIT 1) "
    "GROUP BY Description, Country "
    "ORDER BY QuantidadeTotal DESC LIMIT 1 "
)

for line in cursor.fetchall():
    print(f"O país com maior volume de vendas foi {line[0]} e o item mais vendido foi {line[1]} com {line[2]} unidades comercializadas")

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