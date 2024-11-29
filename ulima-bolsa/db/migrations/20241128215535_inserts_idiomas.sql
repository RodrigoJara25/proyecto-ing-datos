-- migrate:up
INSERT INTO idiomas (id, nombre, nivel) VALUES (1, 'Ingles',	'Basico');
INSERT INTO idiomas (id, nombre, nivel) VALUES (2, 'Ingles',	'Intermedio');
INSERT INTO idiomas (id, nombre, nivel) VALUES (3, 'Ingles',	'Avanzado');
INSERT INTO idiomas (id, nombre, nivel) VALUES (4, 'Español',	'Basico');
INSERT INTO idiomas (id, nombre, nivel) VALUES (5, 'Español',	'Intermedio');
INSERT INTO idiomas (id, nombre, nivel) VALUES (6, 'Español',	'Avanzado');
INSERT INTO idiomas (id, nombre, nivel) VALUES (7, 'Frances',	'Basico');
INSERT INTO idiomas (id, nombre, nivel) VALUES (8, 'Frances',	'Intermedio');
INSERT INTO idiomas (id, nombre, nivel) VALUES (9, 'Frances',	'Avanzado');
INSERT INTO idiomas (id, nombre, nivel) VALUES (10, 'Aleman',	'Basico');
INSERT INTO idiomas (id, nombre, nivel) VALUES (11, 'Aleman',	'Intermedio');
INSERT INTO idiomas (id, nombre, nivel) VALUES (12, 'Aleman',	'Avanzado');
INSERT INTO idiomas (id, nombre, nivel) VALUES (13, 'Portugues',	'Basico');
INSERT INTO idiomas (id, nombre, nivel) VALUES (14, 'Portugues',	'Intermedio');
INSERT INTO idiomas (id, nombre, nivel) VALUES (15, 'Portugues',	'Avanzado');

-- migrate:down
DELETE FROM idiomas;
