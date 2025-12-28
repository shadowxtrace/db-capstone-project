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

# Step 2: Drop procedure if it already exists
cursor.execute("DROP PROCEDURE IF EXISTS GetMaxQuantity;")
connection.commit()
print("Old GetMaxQuantity procedure dropped (if it existed)")

# Step 3: Create the stored procedure
create_procedure_sql = """
CREATE PROCEDURE GetMaxQuantity()
BEGIN
    SELECT MAX(Quantity) AS 'Max Quantity in Order'
    FROM Orders;
END;
"""
cursor.execute(create_procedure_sql)
connection.commit()
print("Stored procedure GetMaxQuantity created")

# Step 4: Call the stored procedure
cursor.callproc("GetMaxQuantity")

print("Procedure result:")
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

# Step 5: Close connection
cursor.close()
connection.close()
print("Done")
