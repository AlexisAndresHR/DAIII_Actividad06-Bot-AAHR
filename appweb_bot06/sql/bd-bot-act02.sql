CREATE DATABASE fut_bot06;

USE fut_bot06;

CREATE TABLE jugadores(
    numero int NOT NULL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    pais varchar(30) NOT NULL,
    posicion varchar(30) NOT NULL,
    equipo varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO jugadores (numero, nombre, pais, posicion, equipo) VALUES 
(1, 'Hugo Lloris', 'Francia', 'Portero', 'Tottenham Hotspur'),
(2, 'Diego Godín', 'Uruguay', 'Defensa central', 'Atlético de Madrid'),
(3, 'Gerard Piqué', 'España', 'Defensa central', 'FC Barcelona');

SHOW TABLES;
DESCRIBE jugadores;

SELECT * FROM jugadores;

CREATE USER 'futbot'@'localhost' IDENTIFIED BY 'futbot.2019';
GRANT ALL PRIVILEGES ON fut_bot06.* TO 'futbot'@'localhost';
FLUSH PRIVILEGES;
