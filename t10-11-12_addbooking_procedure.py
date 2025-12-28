import mysql.connector as connector

connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")

cursor.execute("DROP PROCEDURE IF EXISTS AddBooking;")
cursor.execute("""
CREATE PROCEDURE AddBooking(
    IN p_BookingID INT,
    IN p_CustomerID INT,
    IN p_TableNumber INT,
    IN p_BookingDate DATE
)
BEGIN
    INSERT INTO Bookings (BookingID, BookingDate, TableNumber, CustomerID)
    VALUES (p_BookingID, p_BookingDate, p_TableNumber, p_CustomerID);

    SELECT 'New booking added' AS Confirmation;
END;
""")
connection.commit()

cursor.callproc("AddBooking", [9, 3, 4, "2022-12-30"])
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

cursor.execute("DROP PROCEDURE IF EXISTS UpdateBooking;")
cursor.execute("""
CREATE PROCEDURE UpdateBooking(
    IN p_BookingID INT,
    IN p_BookingDate DATE
)
BEGIN
    UPDATE Bookings
    SET BookingDate = p_BookingDate
    WHERE BookingID = p_BookingID;

    SELECT CONCAT('Booking ', p_BookingID, ' updated') AS Confirmation;
END;
""")
connection.commit()

cursor.callproc("UpdateBooking", [9, "2022-12-17"])
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

cursor.execute("DROP PROCEDURE IF EXISTS CancelBooking;")
cursor.execute("""
CREATE PROCEDURE CancelBooking(
    IN p_BookingID INT
)
BEGIN
    DELETE FROM Bookings
    WHERE BookingID = p_BookingID;

    SELECT CONCAT('Booking ', p_BookingID, ' cancelled') AS Confirmation;
END;
""")
connection.commit()

cursor.callproc("CancelBooking", [9])
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

cursor.close()
connection.close()
