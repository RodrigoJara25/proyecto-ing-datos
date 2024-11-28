-- migrate:up
CREATE TABLE distritos (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(30) NOT NULL,
  provincia_id INTEGER NOT NULL,
  FOREIGN KEY (provincia_id) REFERENCES provincias (id)
);

-- migrate:down
DROP TABLE distritos;
