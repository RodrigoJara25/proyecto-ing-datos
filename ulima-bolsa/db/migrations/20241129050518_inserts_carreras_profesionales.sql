-- migrate:up
INSERT INTO carreras_profesionales (id, nombre) VALUES (1, 'Administración');
INSERT INTO carreras_profesionales (id, nombre) VALUES (2, 'Arquitectura');
INSERT INTO carreras_profesionales (id, nombre) VALUES (3, 'Comunicación');
INSERT INTO carreras_profesionales (id, nombre) VALUES (4, 'Contabilidad');
INSERT INTO carreras_profesionales (id, nombre) VALUES (5, 'Derecho');
INSERT INTO carreras_profesionales (id, nombre) VALUES (6, 'Economía');
INSERT INTO carreras_profesionales (id, nombre) VALUES (7, 'Ingeniería Civil');
INSERT INTO carreras_profesionales (id, nombre) VALUES (8, 'Ingeniería de Sistemas');
INSERT INTO carreras_profesionales (id, nombre) VALUES (9, 'Ingeniería Industrial');
INSERT INTO carreras_profesionales (id, nombre) VALUES (10, 'Marketing');
INSERT INTO carreras_profesionales (id, nombre) VALUES (11, 'Negocios Internacionales');
INSERT INTO carreras_profesionales (id, nombre) VALUES (12, 'Psicología');

-- migrate:down
DELETE FROM carreras_profesionales;
