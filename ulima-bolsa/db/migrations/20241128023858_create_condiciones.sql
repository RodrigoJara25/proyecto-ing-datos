-- migrate:up
CREATE TABLE condiciones (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(40) NOT NULL
);

-- migrate:down
DROP TABLE condiciones;