-- migrate:up
CREATE TABLE modalidades (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL
);

-- migrate:down
DROP TABLE modalidades;