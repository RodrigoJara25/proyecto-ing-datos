-- migrate:up
CREATE TABLE experiencias (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  tiempo INTEGER NOT NULL,
  descripcion VARCHAR(200)
);

-- migrate:down
DROP TABLE experiencias;