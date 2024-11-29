-- migrate:up
INSERT INTO disponibilidad_horarios (id, nombre) VALUES (1,	'TIEMPO COMPLETO');
INSERT INTO disponibilidad_horarios (id, nombre) VALUES (2,	'TIEMPO PARCIAL');

-- migrate:down
DELETE FROM disponiblidad_horarios;