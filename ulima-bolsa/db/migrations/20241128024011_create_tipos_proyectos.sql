-- migrate:up
CREATE TABLE tipos_proyectos (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(15) NOT NULL
);

-- migrate:down
DROP TABLE tipos_proyectos;