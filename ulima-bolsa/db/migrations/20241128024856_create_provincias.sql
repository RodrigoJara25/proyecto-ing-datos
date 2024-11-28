-- migrate:up
CREATE TABLE provincias (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(30) NOT NULL,
  departamento_id INTEGER NOT NULL,
  FOREIGN KEY (departamento_id) REFERENCES departamentos (id)
);

-- migrate:down
DROP TABLE provincias;
