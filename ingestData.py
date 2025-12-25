from productDetails import product
from dbConnection import conn,cursor

# print(product)
price = int(product["price"].replace(",", ""))
rating = float(product["rating"])
rating_count = int(product["rating_count"].replace("(", "").replace(")", "").replace(",", ""))


insert_query = """
INSERT INTO products
(name, brand, price, rating, rating_count, image_url)
VALUES (%s, %s, %s, %s, %s, %s)
"""

values = (
    product["name"],
    product["brand"],
    price,
    rating,
    rating_count,
    product["image_url"]
)

cursor.execute(insert_query, values)
conn.commit()

print("Product inserted successfully")
