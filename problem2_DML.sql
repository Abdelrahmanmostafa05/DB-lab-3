USE library;

INSERT INTO AUTHOR (author_id, name, country) VALUES
(1, 'Naguib Mahfouz',  'Egypt'),
(2, 'George Orwell',   'United Kingdom'),
(3, 'Agatha Christie', 'United Kingdom');

INSERT INTO BOOK (book_id, title, price, author_id) VALUES
(1, 'Palace Walk',                  15.50, 1),
(2, 'Sugar Street',                 14.00, 1),
(3, '1984',                         12.99, 2),
(4, 'Animal Farm',                   9.99, 2),
(5, 'And Then There Were None',     11.50, 3),
(6, 'Murder on the Orient Express', 13.20, 3);
