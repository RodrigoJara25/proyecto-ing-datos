-- migrate:up
CREATE TABLE ciclos (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ciclo INTEGER NOT NULL
);

-- migrate:down
DROP TABLE ciclos;