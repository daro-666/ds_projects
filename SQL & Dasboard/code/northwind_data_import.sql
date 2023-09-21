\c northwind


DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories (
categoryID INT PRIMARY KEY,
categoryName VARCHAR,
decription VARCHAR,
picture VARCHAR
);

\copy categories FROM '../data/categories.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers (
customerID VARCHAR PRIMARY KEY,
companyName VARCHAR,
contactName VARCHAR,
contactTitle VARCHAR,
address VARCHAR,
city VARCHAR,
region VARCHAR,
postalCode VARCHAR,
country VARCHAR,
phone VARCHAR,
fax VARCHAR
);

\copy customers FROM '../data/customers.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS employee_territories;
CREATE TABLE IF NOT EXISTS employee_territories (
employeeID INT ,
territoryID INT PRIMARY KEY
);

\copy employee_territories FROM '../data/employee_territories.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS employees;
CREATE TABLE IF NOT EXISTS employees (
employeeID INT PRIMARY KEY,
lastName VARCHAR,
firstName VARCHAR,
title VARCHAR,
titleOfCourtesy VARCHAR,
birthDate TIMESTAMP,
hireDate TIMESTAMP,
address VARCHAR,
city VARCHAR,
region VARCHAR,
postalCode VARCHAR,
country VARCHAR,
homePhone VARCHAR,
extension VARCHAR,
photo VARCHAR,
notes VARCHAR,
reportsTo VARCHAR,
photoPath VARCHAR
);

\copy employees FROM '../data/employees.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS order_details;
CREATE TABLE IF NOT EXISTS order_details (
orderID INT,
productID INT,
unitPrice NUMERIC,
quantity INT,
discount NUMERIC
);

\copy order_details FROM '../data/order_details.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders (
orderID INT PRIMARY KEY,
customerID VARCHAR,
employeeID INT,
orderDate TIMESTAMP,
requiredDate TIMESTAMP,
shippedDate TIMESTAMP,
shipVia INT,
freight NUMERIC,
shipName VARCHAR,
shipAddress VARCHAR,
shipCity VARCHAR,
shipRegion VARCHAR,
shipPostalCode VARCHAR,
shipCountry VARCHAR
);

\copy orders FROM '../data/orders.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS products;
CREATE TABLE IF NOT EXISTS products (
productID INT PRIMARY KEY,
productName VARCHAR,
supplierID INT,
categoryID INT,
quantityPerUnit VARCHAR,
unitPrice NUMERIC,
unitsInStock INT,
unitsOnOrder INT,
reorderLevel INT,
discontinued INT
);

\copy products FROM '../data/products.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS regions;
CREATE TABLE IF NOT EXISTS regions (
regionID INT PRIMARY KEY,
regionDescription VARCHAR
);

\copy regions FROM '../data/regions.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS shippers;
CREATE TABLE IF NOT EXISTS shippers (
shipperID INT PRIMARY KEY,
companyName VARCHAR,
phone VARCHAR
);

\copy shippers FROM '../data/shippers.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS suppliers;
CREATE TABLE IF NOT EXISTS suppliers (
supplierID INT PRIMARY KEY,
companyName VARCHAR,
contactName VARCHAR,
contactTitle VARCHAR,
address VARCHAR,
city VARCHAR,
region VARCHAR,
postalCode VARCHAR,
country VARCHAR,
phone VARCHAR,
fax VARCHAR,
homePage VARCHAR
);

\copy suppliers FROM '../data/suppliers.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


DROP TABLE IF EXISTS territories;
CREATE TABLE IF NOT EXISTS territories (
territoryID INT PRIMARY KEY,
territoryDescription VARCHAR,
regionID INT
);

\copy territories FROM '../data/territories.csv' DELIMITER ',' CSV HEADER NULL AS 'NULL'


--SELECT * FROM territories;
\d