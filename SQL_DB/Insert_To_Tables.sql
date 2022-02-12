INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Naor', '1995-08-03', 'Naor@gmail.com', '0529984751','123');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Orit', '1995-09-06', 'Orit@gmail.com', '0529984767','234');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Matan', '1995-09-19', 'Matan@gmail.com', '0529984465','345');

INSERT INTO users (Name, BirthDate, Email, Phone_number, Password)
VALUES ('Shiran', '1996-10-02', 'Shiran@gmail.com', '0547561465','456');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('6','Ariel','1985-08-03', 'ariel@gmail.com','0546645819','ariel');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('7','Eti','1980-03-03', 'eti@gmail.com','0522977826','eti1');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('8','Stav','1994-11-05', 'stav@gmail.com','0523565680','stav11');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('9','Amit','2000-08-14', 'amit@gmail.com','0546633819','amit14');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Food Basket', 'Food', '120', 'wine, rice, oil, sugar, flour, tuna, cans, pasta','../static/media/foodbasket.jpg');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Hot food', 'Food', '40', 'Single hot meal for one person','../static/media/warmfood.jpg');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Candies Basket', 'Food', '60', 'chocolates and snacks packages to put a big smile on thier face','../static/media/candis.png');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Pillows and Blankets', 'Clothes and Home', '250', 'Pillow x 2 Blanket x 1','../static/media/PillowsAndBlankets2.jfif');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Pots and pans', 'Clothes and Home', '200', 'Pot x 3 sizes- S,M,L Pan x 2 size M','../static/media/PotsAndPans.jfif');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('Pajamas', 'Clothes and Home', '100', '2 sets of pajamas ,(for male or female)','../static/media/Pjs.png');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('100 NIS', 'Cash Donation', '100', '10% will be added by the organization','../static/media/CashPic.jpg');

INSERT INTO products  (Name, Category, Price, Description,Photo)
VALUES ('Your Choice', 'Cash Donation','1', '10% will be added by the organization','../static/media/CashPic.jpg');

INSERT INTO products (Name, Category, Price, Description,Photo)
VALUES ('200 NIS', 'Cash Donation', '200', '10% will be added by the organization','../static/media/CashPic.jpg');

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
