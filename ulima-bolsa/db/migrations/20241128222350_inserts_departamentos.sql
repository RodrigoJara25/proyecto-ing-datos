-- migrate:up
INSERT INTO departamentos (id, nombre) VALUES (1, 'Amazonas');
INSERT INTO departamentos (id, nombre) VALUES (2, 'Ancash');
INSERT INTO departamentos (id, nombre) VALUES (3, 'Apurimac');
INSERT INTO departamentos (id, nombre) VALUES (4, 'Arequipa');
INSERT INTO departamentos (id, nombre) VALUES (5, 'Ayacucho');
INSERT INTO departamentos (id, nombre) VALUES (6, 'Cajamarca');
INSERT INTO departamentos (id, nombre) VALUES (7, 'Callao');
INSERT INTO departamentos (id, nombre) VALUES (8, 'Cusco');
INSERT INTO departamentos (id, nombre) VALUES (9, 'Huancavelica');
INSERT INTO departamentos (id, nombre) VALUES (10, 'Huanuco');
INSERT INTO departamentos (id, nombre) VALUES (11, 'Ica');
INSERT INTO departamentos (id, nombre) VALUES (12, 'Junin');
INSERT INTO departamentos (id, nombre) VALUES (13, 'La Libertad');
INSERT INTO departamentos (id, nombre) VALUES (14, 'Lambayeque');
INSERT INTO departamentos (id, nombre) VALUES (15, 'Lima');
INSERT INTO departamentos (id, nombre) VALUES (16, 'Loreto');
INSERT INTO departamentos (id, nombre) VALUES (17, 'Madre de Dios');
INSERT INTO departamentos (id, nombre) VALUES (18, 'Moquegua');
INSERT INTO departamentos (id, nombre) VALUES (19, 'Pasco');
INSERT INTO departamentos (id, nombre) VALUES (20, 'Piura');
INSERT INTO departamentos (id, nombre) VALUES (21, 'Puno');
INSERT INTO departamentos (id, nombre) VALUES (22, 'San Martin');
INSERT INTO departamentos (id, nombre) VALUES (23, 'Tacna');
INSERT INTO departamentos (id, nombre) VALUES (24, 'Tumbes');
INSERT INTO departamentos (id, nombre) VALUES (25, 'Ucayali');

-- migrate:down
DELETE FROM departamentos;
