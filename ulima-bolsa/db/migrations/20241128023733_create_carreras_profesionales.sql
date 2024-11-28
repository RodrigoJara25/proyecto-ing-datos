-- migrate:up
CREATE TABLE carreras_profesionales (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL
);

-- migrate:down
DROP TABLE carreras_profesionales;