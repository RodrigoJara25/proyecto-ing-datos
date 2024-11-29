-- migrate:up
INSERT INTO condiciones (id, nombre) VALUES (1, 'BACHILLER');
INSERT INTO condiciones (id, nombre) VALUES (2, 'EGRESADO');
INSERT INTO condiciones (id, nombre) VALUES (3, 'ALUMNO/NIVEL 4');
INSERT INTO condiciones (id, nombre) VALUES (4, 'ALUMNO/NIVEL 5');
INSERT INTO condiciones (id, nombre) VALUES (5, 'ALUMNO/NIVEL 6');
INSERT INTO condiciones (id, nombre) VALUES (6, 'ALUMNO/NIVEL 7');
INSERT INTO condiciones (id, nombre) VALUES (7, 'ALUMNO/NIVEL 8');
INSERT INTO condiciones (id, nombre) VALUES (8, 'ALUMNO/NIVEL 9');
INSERT INTO condiciones (id, nombre) VALUES (9, 'ALUMNO/NIVEL 10');

-- migrate:down
DELETE FROM condiciones;
