import mysql.connector as connector

connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")

# 1) Create the required parent rows (customers) FIRST
cursor.execute("""
INSERT INTO CustomerDetails (CustomerID, FirstName, LastName, Phone, Email)
VALUES
(1, 'Vanessa', 'McCarthy', '555-0101', 'vanessa@example.com'),
(2, 'Marcos', 'Romero',   '555-0102', 'marcos@example.com'),
(3, 'Ava',    'Johnson',  '555-0103', 'ava@example.com')
ON DUPLICATE KEY UPDATE
FirstName=VALUES(FirstName),
LastName=VALUES(LastName),
Phone=VALUES(Phone),
Email=VALUES(Email);
""")

# 2) Now insert the bookings
cursor.execute("""
INSERT INTO Bookings (BookingID, BookingDate, TableNumber, CustomerID)
VALUES
(1, '2022-10-10', 5, 1),
(2, '2022-11-12', 3, 3),
(3, '2022-10-11', 2, 2),
(4, '2022-10-13', 2, 1)
ON DUPLICATE KEY UPDATE
BookingDate=VALUES(BookingDate),
TableNumber=VALUES(TableNumber),
CustomerID=VALUES(CustomerID);
""")

connection.commit()

# Verify
cursor.execute("SELECT * FROM Bookings ORDER BY BookingID;")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
print("Done")
