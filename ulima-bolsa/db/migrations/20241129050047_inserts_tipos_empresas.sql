-- migrate:up
INSERT INTO tipos_empresas (id, nombre) VALUES (1, 'Publica');
INSERT INTO tipos_empresas (id, nombre) VALUES (2, 'Privada');
INSERT INTO tipos_empresas (id, nombre) VALUES (3, 'Con fines de lucro');
INSERT INTO tipos_empresas (id, nombre) VALUES (4, 'Sin fines de lucro');

-- migrate:down
DELETE FROM tipos_empresas;
