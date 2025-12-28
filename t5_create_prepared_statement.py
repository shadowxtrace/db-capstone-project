import mysql.connector as connector

# Step 1: Connect to MySQL
connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")
print("Connected to LittleLemonDB")

# Step 2: Deallocate prepared statement if it already exists
# (MySQL requires this pattern for prepared statements)
try:
    cursor.execute("DEALLOCATE PREPARE GetOrderDetail;")
except:
    pass

# Step 3: Create the prepared statement
prepare_sql = """
PREPARE GetOrderDetail FROM
'SELECT OrderID, Quantity, TotalCost AS Cost
 FROM Orders
 WHERE CustomerID = ?';
"""
cursor.execute(prepare_sql)
print("Prepared statement GetOrderDetail created")

# Step 4: Set variable and execute prepared statement
cursor.execute("SET @id = 1;")
cursor.execute("EXECUTE GetOrderDetail USING @id;")

# Fetch and display results
rows = cursor.fetchall()
print("Prepared statement result:")
for row in rows:
    print(row)

# Step 5: Clean up
cursor.execute("DEALLOCATE PREPARE GetOrderDetail;")
connection.commit()

cursor.close()
connection.close()
print("Done")
