CREATE TABLE Estudiantes (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Edad INT,
    Telefono VARCHAR(15)
);

INSERT INTO Estudiantes (Id, Nombre, Apellido, Edad, Telefono)
VALUES
(1, 'Carlos', 'Bruzual', 18, '+584141068644'),
(2, 'Jose', 'Colina', 18, '+584265517015'),
(3, 'Miguel', 'Gomez', 18, '+584241065043'),
(4, 'Victor', 'Rodriguez', 19, '+584269787140'),
(5, 'Jean', 'Cefala', 18, '+584127073073'),
(6, 'Jaiver', 'Camacho', 17, '+584121343359'),
(7, 'Diego', 'Hernandez', 17, '+584246148577'),
(8, 'Nestor', 'Nuñez', 18, '+584247830571'),
(9, 'Sebastian', 'Medina', 18, '+584262250894'),
(10, 'Ezequiel', 'Garcia', 18, '+584122811762'),
(11, 'Samuel', 'Alvarado', 18, '+584247493731'),
(12, 'Roque', 'Oviedo', 18, '+584126887982');

SELECT Id, Nombre, Apellido, Edad, Telefono FROM Estudiantes;