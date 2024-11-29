-- migrate:up
INSERT INTO tipos_ofertas (id, nombre) VALUES (1, 'Otras Oportunidades');
INSERT INTO tipos_ofertas (id, nombre) VALUES (2, 'Empleos');
INSERT INTO tipos_ofertas (id, nombre) VALUES (3, 'Practicas Pre Profesionales');

-- migrate:down
DELETE FROM tipos_ofertas;
