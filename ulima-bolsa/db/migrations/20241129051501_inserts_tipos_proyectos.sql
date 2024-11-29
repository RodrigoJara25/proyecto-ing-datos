-- migrate:up
INSERT INTO tipos_proyectos (id, nombre) VALUES (1,	'Curso');
INSERT INTO tipos_proyectos (id, nombre) VALUES (2,	'Trabajo');
INSERT INTO tipos_proyectos (id, nombre) VALUES (3,	'Personal');

-- migrate:down
DELETE FROM tipos_proyectos;
