CREATE TABLE COMITE (
    ID_COMITE INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30),
    CI CHAR(10),
    FECHA_NACIMIENTO DATE,
    GENERO VARCHAR(15),
    ROL VARCHAR(15) NOT NULL,
    CODIGO VARCHAR(15)
);
CREATE TABLE ELECTOR (
    ID_ELECTOR INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30),
    CI CHAR(10),
    FECHA_NACIMIENTO DATE,
    GENERO VARCHAR(15),
    ESTADO_HABILITADO INT NOT NULL
);
CREATE TABLE CANDIDATO (
    ID_CANDIDATO INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30),
    CI CHAR(10),
    FECHA_NACIMIENTO DATE,
    GENERO VARCHAR(15),
    votos INT,
    FOTO VARCHAR(50) NOT NULL,
    PARTIDO VARCHAR(20) NOT NULL,
    COLOR VARCHAR(15)
);

INSERT INTO COMITE (ID_COMITE, NOMBRE, CI, FECHA_NACIMIENTO, GENERO, ROL, CODIGO) VALUES
(1, 'Juan Pérez', '1234567', '1990-05-15', 'Masculino', 'Presidente', 'JP1234'),
(2, 'Ana Soto', '4567890', '1995-03-07', 'Femenino', 'Vocal', 'AS4567'),
(3, 'Carlos Gutiérrez', '3456789', '1978-11-10', 'Masculino', 'Vocal', 'CG3456'),
(4, 'Javier Rodríguez', '7890123', '1975-12-03', 'Masculino', 'Vocal', 'JR7890'),
(5, 'Luisa Gómez', '6789012', '1989-04-25', 'Femenino', 'Secretario', 'LG6789'),
(6, 'María López', '2345678', '1985-08-22', 'Femenino', 'Secretario', 'ML2345'),
(7, 'Miguel Vargas', '9012345', '1980-10-30', 'Masculino', 'Vocal', 'MV9012'),
(8, 'Pedro Mendoza', '5678901', '1982-09-18', 'Masculino', 'Vocal', 'PM5678'),
(9, 'Rosa Martínez', '8901234', '1998-07-14', 'Femenino', 'Secretario', 'RM8901'),
(10, 'Sofía Herrera', '0123456', '1993-06-08', 'Femenino', 'Presidente', 'SH0123');

INSERT INTO CANDIDATO (ID_CANDIDATO, NOMBRE, CI, FECHA_NACIMIENTO, GENERO, votos, FOTO, PARTIDO, COLOR) VALUES
(1, 'Obama', '97', '1990-10-01', 'Masculino', 3, 'obama.jpg', 'KML', '#02ac66'),
(2, 'Vladimir Putin', '98', '1990-11-01', 'Masculino', 6, 'putin.jpg', 'XYZ', '#024a86'),
(3, 'Manfred Reyes', '99', '1990-12-01', 'Masculino', 13, 'manfred.jpg', 'RQT', '#7f00b2'),
(4, 'NULO', NULL, NULL, NULL, 3, 'NULO.png', 'NULO', NULL),
(5, 'BLANCO', NULL, NULL, NULL, 2, 'Blanco.png', 'BLANCO', NULL);

INSERT INTO ELECTOR (NOMBRE, CI, FECHA_NACIMIENTO, GENERO, ESTADO_HABILITADO)
VALUES 
    ('Juan Pérez', '1234567', '1990-01-15', 'Masculino', 1),
    ('María Gutiérrez', '9876543', '1985-05-22', 'Femenino', 1),
    ('Carlos Vargas', '5678901', '1982-11-08', 'Masculino', 1),
    ('Luisa Fernández', '3456789', '1993-07-03', 'Femenino', 1),
    ('Pedro Martínez', '2345678', '1978-09-12', 'Masculino', 1);