import mysql.connector as connector

connection = connector.connect(
    user="root",
    password="root1234",
    host="localhost",
    port=3306
)

cursor = connection.cursor()
cursor.execute("USE LittleLemonDB;")

# Drop if exists
cursor.execute("DROP PROCEDURE IF EXISTS CheckBooking;")
connection.commit()

# Create procedure
create_proc_sql = """
CREATE PROCEDURE CheckBooking(
    IN booking_date DATE,
    IN table_number INT
)
BEGIN
    DECLARE booking_count INT;

    SELECT COUNT(*) INTO booking_count
    FROM Bookings
    WHERE BookingDate = booking_date
      AND TableNumber = table_number;

    IF booking_count > 0 THEN
        SELECT CONCAT('Table ', table_number, ' is already booked') AS 'Booking status';
    ELSE
        SELECT CONCAT('Table ', table_number, ' is available') AS 'Booking status';
    END IF;
END;
"""
cursor.execute(create_proc_sql)
connection.commit()

# Test call
cursor.callproc("CheckBooking", ['2022-11-12', 3])
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

cursor.close()
connection.close()
