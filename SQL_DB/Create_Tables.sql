create schema web_project_g8;

use web_project_g8;

#DROP TABLE Users;
CREATE TABLE Users(
  User_id int auto_increment primary key,
  Name varchar(120),
  BirthDate date,
  Email varchar(255),
  Phone_number varchar(10),
  Password varchar(255)
);

#DROP TABLE Products;
CREATE TABLE Products(
  Product_id int auto_increment primary key,
  Name varchar(120),
  Category varchar(120),
  Price int,
  Description varchar(500),
  Photo varchar(255)
);

#DROP TABLE Organizations;
CREATE TABLE Organizations (
  Org_id int auto_increment primary key,
  Name varchar(120),
  Description varchar(500)
);

#DROP TABLE Donations;
CREATE TABLE Donations (
  Donation_id int auto_increment ,
  Product_id int,
  User_id int,
  Donation_DT timestamp default CURRENT_TIMESTAMP,
  Quantity int,
  Ordered int default 0,

  constraint pk_donations primary key (Donation_id, Product_id),
  constraint fk_users foreign key (User_id) references users (User_id),
  constraint fk_products foreign key (Product_id) references products (Product_id)
);


#DROP TABLE Credit_Cards;
CREATE TABLE Credit_Cards (
  CC_Number varchar(25),
  User_id int,
  CC_Holder_id varchar(12),
  Expire_month int,
  Expire_year int,
  CVC varchar(3),

  constraint pk_CC primary key (CC_Number),
  constraint fk_users_CC foreign key (User_id) references users (User_id)
);

#DROP Table Events;
CREATE TABLE Events (
  Event_id int auto_increment primary key,
  Org_id int,
  Event_name varchar(120),
  Capacity int,
  Event_date datetime,

  constraint fk_organizations foreign key (Org_id) references organizations (Org_id)
);


#DROP TABLE Event_Participants;
CREATE TABLE Event_Participants (
  Event_id int,
  User_id int,
  Create_date timestamp default CURRENT_TIMESTAMP,

  constraint pk_participants primary key (Event_id, User_id),
  constraint fk_events foreign key (Event_id) references web_project_g8.events (Event_id),
  constraint fk_users_participants foreign key (User_id) references users (User_id)
);