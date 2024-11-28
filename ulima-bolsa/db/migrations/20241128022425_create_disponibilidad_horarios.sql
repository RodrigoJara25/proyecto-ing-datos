-- migrate:up
CREATE TABLE disponibilidad_horarios (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL
);

-- migrate:down
DROP TABLE disponibilidad_horarios;