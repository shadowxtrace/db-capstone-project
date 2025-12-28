import mysql.connector as connector

connection = connector.connect(
    user = "root",
    password = "root1234",
    host = "localhost",
    port = 3306
)

cursor = connection.cursor()
print("Cursor is Live!")

drop_db = "DROP DATABASE IF EXISTS LittleLemonDB;"
cursor.execute(drop_db)

create_db = "CREATE DATABASE LittleLemonDB;"
cursor.execute(create_db)

use_db = "USE LittleLemonDB;"
cursor.execute(use_db)

create_customer_details = """
CREATE TABLE CustomerDetails (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName  VARCHAR(50) NOT NULL,
    Phone     VARCHAR(20) NOT NULL,
    Email     VARCHAR(100),
    UNIQUE (Email)
);
"""
cursor.execute(create_customer_details)

create_staff_information = """
CREATE TABLE StaffInformation (
    StaffID   INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName  VARCHAR(50) NOT NULL,
    Role      VARCHAR(50) NOT NULL,
    Salary    DECIMAL(10,2) NOT NULL
);
"""
cursor.execute(create_staff_information)

create_menu = """
CREATE TABLE Menu (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY,
    ItemName   VARCHAR(100) NOT NULL,
    Category   VARCHAR(20) NOT NULL,
    Cuisine    VARCHAR(50) NOT NULL,
    Price      DECIMAL(10,2) NOT NULL
);
"""
cursor.execute(create_menu)

create_bookings = """
CREATE TABLE Bookings (
    BookingID   INT AUTO_INCREMENT PRIMARY KEY,
    BookingDate DATE NOT NULL,
    TableNumber INT NOT NULL,
    CustomerID  INT NOT NULL,
    CONSTRAINT fk_bookings_customer
        FOREIGN KEY (CustomerID) REFERENCES CustomerDetails(CustomerID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
"""
cursor.execute(create_bookings)

create_orders = """
CREATE TABLE Orders (
    OrderID    INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate  DATE NOT NULL,
    Quantity   INT NOT NULL,
    TotalCost  DECIMAL(10,2) NOT NULL,
    CustomerID INT NOT NULL,
    StaffID    INT,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (CustomerID) REFERENCES CustomerDetails(CustomerID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_orders_staff
        FOREIGN KEY (StaffID) REFERENCES StaffInformation(StaffID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
"""
cursor.execute(create_orders)

create_order_items = """
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID     INT NOT NULL,
    MenuItemID  INT NOT NULL,
    Quantity    INT NOT NULL,
    LineTotal   DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_orderitems_order
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_orderitems_menu
        FOREIGN KEY (MenuItemID) REFERENCES Menu(MenuItemID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
"""
cursor.execute(create_order_items)

create_order_delivery_status = """
CREATE TABLE OrderDeliveryStatus (
    DeliveryStatusID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID          INT NOT NULL UNIQUE,
    DeliveryDate     DATE,
    Status           VARCHAR(20) NOT NULL,
    CONSTRAINT fk_delivery_order
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
"""
cursor.execute(create_order_delivery_status)

connection.commit()
print("LittleLemonDB created with required table names + normalized OrderItems")

show_tables = "SHOW TABLES;"
cursor.execute(show_tables)
print("Tables:")
for (t,) in cursor.fetchall():
    print(" -", t)

cursor.close()
connection.close()
print("Done")
