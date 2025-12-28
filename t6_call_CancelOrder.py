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
cursor.execute("DROP PROCEDURE IF EXISTS CancelOrder;")
connection.commit()
print("Old CancelOrder procedure dropped (if it existed)")

# Step 3: Create the CancelOrder stored procedure
create_procedure_sql = """
CREATE PROCEDURE CancelOrder(IN order_id INT)
BEGIN
    DELETE FROM Orders
    WHERE OrderID = order_id;

    SELECT CONCAT('Order ', order_id, ' is cancelled') AS Confirmation;
END;
"""
cursor.execute(create_procedure_sql)
connection.commit()
print("Stored procedure CancelOrder created")

# Step 4: Call the procedure (example: cancel order with ID = 5)
cursor.callproc("CancelOrder", [5])

print("Procedure result:")
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

# Step 5: Close connection
cursor.close()
connection.close()
print("Done")
