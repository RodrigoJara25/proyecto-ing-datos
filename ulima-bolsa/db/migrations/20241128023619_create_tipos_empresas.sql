-- migrate:up
CREATE TABLE tipos_empresas (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50)
);

-- migrate:down
DROP TABLE tipos_empresas;