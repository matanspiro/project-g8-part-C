INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Naor', '1995-08-03', 'Naor@gmail.com', '0529984751','123');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Orit', '1995-09-06', 'Orit@gmail.com', '0529984767','234');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Matan', '1995-09-19', 'Matan@gmail.com', '0529984465','345');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Shiran', '1996-10-02', 'Shiran@gmail.com', '0547561465','456');


INSERT INTO products (Name, Category, Price, Description)
VALUES ('Food Basket', 'Food', '120', 'wine, rice, oil, sugar, flour, tuna, cans, pasta');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('Hot food', 'Food', '40', 'Single hot meal for one person');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('Candies Basket', 'Food', '60', 'chocolates and snacks packages to put a big smile on thier face');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('Pillows and Blankets', 'Clothes and Home', '250', 'Pillow x 2 Blanket x 1');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('Pots and pans', 'Clothes and Home', '200', 'Pot x 3 sizes- S,M,L Pan x 2 size M');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('Pajamas', 'Clothes and Home', '100', '2 sets of pajamas ,(for male or female)');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('100 NIS', 'Cash Donation', '100', '10% will be added by the organization');

INSERT INTO products  (Name, Category, Price, Description)
VALUES ('Your Choice', 'Cash Donation','1', '10% will be added by the organization');

INSERT INTO products (Name, Category, Price, Description)
VALUES ('200 NIS', 'Cash Donation', '200', '10% will be added by the organization');

UPDATE products set Photo='../static/media/candis.png' WHERE Product_id=3;
UPDATE products set Photo='../static/media/CashPic.jpg' WHERE Product_id=7;
UPDATE products set Photo='../static/media/CashPic.jpg' WHERE Product_id=8;
UPDATE products set Photo='../static/media/CashPic.jpg' WHERE Product_id=9;
UPDATE products set Photo='../static/media/foodbasket.jpg' WHERE Product_id=1;
UPDATE products set Photo='../static/media/PillowsAndBlankets2.jfif' WHERE Product_id=4;
UPDATE products set Photo='../static/media/Pjs.png' WHERE Product_id=6;
UPDATE products set Photo='../static/media/PotsAndPans.jfif' WHERE Product_id=5;
UPDATE products set Photo='../static/media/warmfood.jpg' WHERE Product_id=2;


INSERT INTO organizations (Name, Description)
VALUES ('Levinshtein Hospital', 'Hospital in Israel');

INSERT INTO organizations (Name, Description)
VALUES ('Center For Sexual Assault Survivors', 'Sexual Assault Survivors center in Israel');

INSERT INTO organizations (Name, Description)
VALUES ('Ahim Gdolim', 'Helping bullied children in Israel');

INSERT INTO organizations (Name, Description)
VALUES ('Beit Miha', 'Founded in 1953, Beit Micha’s mission is to ensure that every infant with hearing loss be fully integrated by first grade: listening, speaking and thriving like any other six-year-old');


INSERT INTO events (Org_id, Event_name, Capacity, Event_date)
VALUES (1, 'Fundraising event for Levinstein Hospital', 200,'2022-01-22 19:30');

INSERT INTO events (Org_id, Event_name, Capacity, Event_date)
VALUES (2, 'Fundraising event for the Center For Sexual Assault Survivors', 200,'2022-04-22 19:30');

INSERT INTO events (Org_id, Event_name, Capacity, Event_date)
VALUES (3, 'Ahim Gdolim fundraising event', 150,'2022-02-22 19:30');

INSERT INTO events (Org_id, Event_name, Capacity, Event_date)
VALUES (4, 'Beit Miha fundraising event', 250,'2022-03-22 19:30');

UPDATE events SET Capacity='1'
