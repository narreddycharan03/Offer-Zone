import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Charan@2001",
    database="amazon_products"
)

cursor = conn.cursor()
print("MySQL Connected Successfully")