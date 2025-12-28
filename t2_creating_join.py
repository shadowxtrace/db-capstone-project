import mysql.connector as connector

connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")

task2_sql = """
SELECT
    cd.CustomerID,
    CONCAT(cd.FirstName, ' ', cd.LastName) AS FullName,
    o.OrderID,
    o.TotalCost AS Cost,
    m.ItemName AS MenuName,
    m.Category
FROM CustomerDetails cd
JOIN Orders o
    ON cd.CustomerID = o.CustomerID
JOIN OrderItems oi
    ON o.OrderID = oi.OrderID
JOIN Menu m
    ON oi.MenuItemID = m.MenuItemID
WHERE o.TotalCost > 150
ORDER BY o.TotalCost ASC;
"""

cursor.execute(task2_sql)
rows = cursor.fetchall()

print("Task 2 results:")
for row in rows:
    print(row)

cursor.close()
connection.close()
