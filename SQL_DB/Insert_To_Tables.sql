-- Users Data
INSERT INTO web_project_g8.users (User_id,Name, BirthDate, Email, Phone_number, Password)
VALUES ('1','Naor Pinto', '1995-08-03', 'Naor@gmail.com', '0526265680','naor');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate, Email, Phone_number, Password)
VALUES ('2','Naor', '1995-08-03', 'Naor@gmail.com', '0529984751','123');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate, Email, Phone_number, Password)
VALUES ('3','Orit', '1995-09-06', 'Orit@gmail.com', '0529984767','234');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate, Email, Phone_number, Password)
VALUES ('4','Matan', '1995-09-19', 'Matan@gmail.com', '0529984465','345');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate, Email, Phone_number, Password)
VALUES ('5','Shiran', '1996-10-02', 'Shiran@gmail.com', '0547561465','456');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('6','Ariel','1985-08-03', 'ariel@gmail.com','0546645819','ariel');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('7','Eti','1980-03-03', 'eti@gmail.com','0522977826','eti1');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('8','Stav','1994-11-05', 'stav@gmail.com','0523565680','stav11');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('9','Amit','2000-08-14', 'amit@gmail.com','0546633819','amit14');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('10','Noam So','1998-02-28', 'noam@gmail.com','0542528801','noam');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('11','Hod Shansha','1995-06-06', 'hod@gmail.com','0526267340','hodhod');

INSERT INTO web_project_g8.users (User_id,Name, BirthDate ,Email,Phone_Number, Password)
 VALUES ('12','Nir','2001-02-02', 'nir@gmail.com','0525378495','nir');

-- Products Data
INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('1','Food Basket', 'Food', '120', 'wine, rice, oil, sugar, flour, tuna, cans, pasta','../static/media/foodbasket.jpg');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('2','Hot food', 'Food', '40', 'Single hot meal for one person','../static/media/warmfood.jpg');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('3','Candies Basket', 'Food', '60', 'chocolates and snacks packages to put a big smile on thier face','../static/media/candis.png');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('4','Pillows and Blankets', 'Clothes and Home', '250', 'Pillow x 2 Blanket x 1','../static/media/PillowsAndBlankets2.jfif');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('5','Pots and pans', 'Clothes and Home', '200', 'Pot x 3 sizes- S,M,L Pan x 2 size M','../static/media/PotsAndPans.jfif');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('6','Pajamas', 'Clothes and Home', '100', '2 sets of pajamas ,(for male or female)','../static/media/Pjs.png');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('7','100 NIS', 'Cash Donation', '100', '10% will be added by the organization','../static/media/CashPic.jpg');

INSERT INTO web_project_g8.products  (Product_id,Name, Category, Price, Description,Photo)
VALUES ('8','Your Choice', 'Cash Donation','1', '10% will be added by the organization','../static/media/CashPic.jpg');

INSERT INTO web_project_g8.products (Product_id,Name, Category, Price, Description,Photo)
VALUES ('9','200 NIS', 'Cash Donation', '200', '10% will be added by the organization','../static/media/CashPic.jpg');

-- Orgs Data
INSERT INTO web_project_g8.organizations (Org_id,Name, Description)
VALUES (1,'Levinshtein Hospital', 'Hospital in Israel');

INSERT INTO web_project_g8.organizations (Org_id,Name, Description)
VALUES (2,'Center For Sexual Assault Survivors', 'Sexual Assault Survivors center in Israel');

INSERT INTO web_project_g8.organizations (Org_id,Name, Description)
VALUES (3,'Ahim Gdolim', 'Helping bullied children in Israel');

INSERT INTO web_project_g8.organizations (Org_id,Name, Description)
VALUES (4,'Beit Miha', 'Founded in 1953, Beit Micha’s mission is to ensure that every infant with hearing loss be fully integrated by first grade: listening, speaking and thriving like any other six-year-old');

-- Events Data
INSERT INTO web_project_g8.events (Event_id,Org_id, Event_name, Capacity, Event_date)
VALUES (1,1, 'Fundraising event for Levinstein Hospital', 200,'2022-01-22 19:30');

INSERT INTO web_project_g8.events (Event_id,Org_id, Event_name, Capacity, Event_date)
VALUES (2,2, 'Fundraising event for the Center For Sexual Assault Survivors', 200,'2022-04-22 19:30');

INSERT INTO web_project_g8.events (Event_id,Org_id, Event_name, Capacity, Event_date)
VALUES (3,3, 'Ahim Gdolim fundraising event', 150,'2022-02-22 19:30');

INSERT INTO web_project_g8.events (Event_id,Org_id, Event_name, Capacity, Event_date)
VALUES (4,4, 'Beit Miha fundraising event', 250,'2022-03-22 19:30');

-- UPDATE events SET Capacity='1';

-- Credit Cards Data
INSERT INTO web_project_g8.credit_cards (CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC)
VALUES ('4443568234567890','7', '3116724389', 6,2026,'324');

INSERT INTO web_project_g8.credit_cards (CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC)
VALUES ('4580000020820111','10', '284637957',12,2024,'123');

INSERT INTO web_project_g8.credit_cards (CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC)
VALUES ('4580030820820444','1', '315625301', 12,2025,'111');

INSERT INTO web_project_g8.credit_cards (CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC)
VALUES ('4580953677142635','8', '274893746', 9,2023,'111');

-- Donations Data
INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (8,1,1, '2022-02-12 10:44:39',2,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (9,1,1, '2022-02-12 12:08:50',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (11,2,10, '2022-02-12 15:17:40',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (12,7,10, '2022-02-12 15:17:42',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (13,5,10, '2022-02-12 15:19:08',1,0);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (17,9,12, '2022-02-12 16:57:59',1,0);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (18,1,7, '2022-02-12 16:58:18',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (19,2,7, '2022-02-12 16:58:22',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (20,3,7, '2022-02-12 16:58:26',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (22,1,6, '2022-02-12 16:59:43',1,0);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (23,2,7, '2022-02-12 17:00:41',1,0);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (24,6,8, '2022-02-12 17:01:28',1,1);

INSERT INTO web_project_g8.donations (Donation_id,Product_id, User_id, Donation_DT, Quantity, Ordered)
VALUES (25,4,8, '2022-02-12 17:01:37',1,1);

-- Event Participants Data
INSERT INTO web_project_g8.event_participants (Event_id,User_id, Create_date)
VALUES (1,10,'2022-02-12 15:17:22');

INSERT INTO web_project_g8.event_participants (Event_id,User_id, Create_date)
VALUES (2,11,'2022-02-12 17:04:17');

INSERT INTO web_project_g8.event_participants (Event_id,User_id, Create_date)
VALUES (3,6,'2022-02-12 16:59:49');

INSERT INTO web_project_g8.event_participants (Event_id,User_id, Create_date)
VALUES (4,7,'2022-02-12 17:00:12');

