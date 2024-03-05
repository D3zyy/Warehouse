CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address_id INT NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address_id INT NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

CREATE TABLE Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL
);

CREATE TABLE Purchases (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    supplier_id INT,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);
