CREATE TABLE planes
(num INTEGER PRIMARY KEY,
Departure CHAR(25),
Arrival CHAR(25)
);

INSERT INTO planes VALUES (5, 'FRANCE','USA');
INSERT INTO planes VALUES (10, 'CANADA','MEXICO');
INSERT INTO planes VALUES (2, 'Spain','Japan');
INSERT INTO planes VALUES (4, 'Russia','India');

SELECT * FROM planes;

SELECT * FROM planes ORDER BY Departure;

SELECT * FROM planes LIMIT 5;