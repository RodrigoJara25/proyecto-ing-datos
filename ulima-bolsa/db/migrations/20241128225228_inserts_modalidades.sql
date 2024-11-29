-- migrate:up
INSERT INTO modalidades (id, nombre) VALUES (1,	'Trabajo presencial');
INSERT INTO modalidades (id, nombre) VALUES (2,	'Trabajo remoto');
INSERT INTO modalidades (id, nombre) VALUES (3,	'Trabajo hibrido');

-- migrate:down
DELETE FROM modalidades;