-- migrate:up
CREATE TABLE idiomas (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(30) NOT NULL,
  nivel VARCHAR(30) NOT NULL
);

-- migrate:down
DROP TABLE idiomas;
