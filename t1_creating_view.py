import mysql.connector as connector

connection = connector.connect(
    user = "root",
    password = "root1234",
    host = "localhost",
    port = 3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")
print("Connected to LittleLemonDB")

create_orders_view = """
CREATE OR REPLACE VIEW OrdersView AS
SELECT
    OrderID,
    Quantity,
    TotalCost AS Cost
FROM Orders
WHERE Quantity > 2;
"""

cursor.execute(create_orders_view)
connection.commit()
print("OrdersView created")

cursor.execute("SELECT * FROM OrdersView;")
rows = cursor.fetchall()

print("OrdersView contents:")
for row in rows:
    print(row)

cursor.close()
connection.close()
print("Done")

