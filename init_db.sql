CREATE DATABASE hotel_campus_db;

USE hotel_campus_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    email VARCHAR(120) NOT NULL
    senha TEXT NOT NULL
);
