-- migrate:up
CREATE TABLE tipos_ofertas (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL
);

-- migrate:down
DROP TABLE tipos_ofertas;