-- migrate:up
CREATE TABLE industrias (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(100)
);

-- migrate:down
DROP TABLE industrias;