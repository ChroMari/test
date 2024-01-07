CREATE DATABASE stock;

USE stock;

CREATE TABLE transport (
  transport_id INT PRIMARY KEY AUTO_INCREMENT,
  uid VARCHAR(10),
  owner VARCHAR(30),
  now_data DATETIME
);