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










