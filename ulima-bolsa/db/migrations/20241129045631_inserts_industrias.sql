-- migrate:up
INSERT INTO industrias (id, nombre) VALUES (1, 'Tecnología');
INSERT INTO industrias (id, nombre) VALUES (2, 'Salud');
INSERT INTO industrias (id, nombre) VALUES (3, 'Educación');
INSERT INTO industrias (id, nombre) VALUES (4, 'Construcción');
INSERT INTO industrias (id, nombre) VALUES (5, 'Finanzas');
INSERT INTO industrias (id, nombre) VALUES (6, 'Energía');
INSERT INTO industrias (id, nombre) VALUES (7, 'Transporte');
INSERT INTO industrias (id, nombre) VALUES (8, 'Turismo');
INSERT INTO industrias (id, nombre) VALUES (9, 'Alimentación');
INSERT INTO industrias (id, nombre) VALUES (10, 'Manufactura');
INSERT INTO industrias (id, nombre) VALUES (11, 'Agricultura');
INSERT INTO industrias (id, nombre) VALUES (12, 'Entretenimiento');
INSERT INTO industrias (id, nombre) VALUES (13, 'Retail');
INSERT INTO industrias (id, nombre) VALUES (14, 'Automotriz');
INSERT INTO industrias (id, nombre) VALUES (15, 'Telecomunicaciones');
INSERT INTO industrias (id, nombre) VALUES (16, 'Minería');
INSERT INTO industrias (id, nombre) VALUES (17, 'Química');
INSERT INTO industrias (id, nombre) VALUES (18, 'Medio ambiente');
INSERT INTO industrias (id, nombre) VALUES (19, 'Logística');
INSERT INTO industrias (id, nombre) VALUES (20, 'Defensa y seguridad');

-- migrate:down
DELETE FROM industrias;
