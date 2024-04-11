-- Kategorie
INSERT INTO Categories (name) VALUES
('Elektronika'),
('Oblečení'),
('Kuchyňské potřeby'),
('Domácí spotřebiče'),
('Sportovní vybavení');

-- Adresy
INSERT INTO Addresses (street, city, postal_code) VALUES
('Hlavní 123', 'Praha', '110 00'),
('Ulice 456', 'Brno', '602 00'),
('Náměstí 789', 'Ostrava', '700 00'),
('Příkladná 12', 'Plzeň', '301 00'),
('Sportovní 24', 'Liberec', '460 00'),
('Parková 7', 'České Budějovice', '370 01'),
('Zahrádkářská 15', 'Olomouc', '779 00'),
('Lesní 3', 'Hradec Králové', '500 09'),
('Vinohradská 88', 'Ústí nad Labem', '400 01'),
('Školní 50', 'Karlovy Vary', '360 05'),
('Jedovnická 2', 'Zlín', '760 01'),
('Purkyňova 30', 'Jihlava', '586 01'),
('Sokolovská 17', 'Pardubice', '532 01'),
('Masarykovo náměstí 1', 'Teplice', '415 01'),
('Smetanova 5', 'Děčín', '405 02');


-- Produkty
INSERT INTO Products (name, category_id, price, quantity) VALUES
('Televize Samsung 50" 4K', 1, 9999, 10),
('Dámský kabát zimní', 2, 1299, 20),
('Kávovar Philips HD8827/09', 3, 1499, 15),
('Mikrovlnná trouba Bosch', 4, 899, 12),
('Posilovací lavice York', 5, 399, 8);

-- Dodavatelé
INSERT INTO Suppliers (name, address_id, contact_number) VALUES
('ElektroWorld s.r.o.', 1, '+420 123 456 789'),
('Modní trendy spol. s.r.o.', 2, '+420 987 654 321'),
('Kuchyňské potřeby a.s.', 3, '+420 111 222 333'),
('Domácí spotřebiče CZ', 4, '+420 444 555 666'),
('Sportovní vybavení Plus', 5, '+420 777 888 999');

-- Zákazníci
INSERT INTO Customers (name, address_id, contact_number) VALUES
('Jan Novák', 6, '+420 111 222 333'),
('Marie Kovářová', 7, '+420 444 555 666'),
('Petr Dvořák', 8, '+420 777 888 999'),
('Eva Procházková', 9, '+420 987 654 321'),
('Tomáš Svoboda', 10, '+420 123 456 789');



-- Nákupy
INSERT INTO Purchases (product_id, supplier_id, quantity, price, date) VALUES
(1, 1, 5, 8999, '2024-03-01'),
(2, 2, 10, 1200, '2024-03-02'),
(3, 3, 8, 1399, '2024-03-03'),
(4, 4, 6, 850, '2024-03-04'),
(5, 5, 3, 349, '2024-03-05');

-- Prodeje
INSERT INTO Sales (product_id, customer_id, quantity, price, date) VALUES
(1, 1, 1, 9999, '2024-03-01'),
(2, 2, 2, 1299, '2024-03-02'),
(3, 3, 1, 1499, '2024-03-03'),
(4, 4, 2, 899, '2024-03-04'),
(5, 5, 1, 399, '2024-03-05');

-- Role
INSERT INTO Roles (name) VALUES
('Admin'),
('Manager'),
('Employee'),
('Guest');

-- Uživatelé
INSERT INTO Users (username, password, role_id) VALUES
('admin', 'admin', 1),
('manager', 'manager', 2),
('employee', 'employee', 3),
('guest', 'guest', 4);

