import mysql.connector as connector

connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")

task3_sql = """
SELECT
    ItemName
FROM Menu
WHERE MenuItemID = ANY (
    SELECT MenuItemID
    FROM OrderItems
    WHERE Quantity > 2
);
"""

cursor.execute(task3_sql)
rows = cursor.fetchall()

print("Task 3 results:")
for row in rows:
    print(row)

cursor.close()
connection.close()
