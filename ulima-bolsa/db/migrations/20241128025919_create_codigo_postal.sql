-- migrate:up
CREATE TABLE codigo_postal (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  numero INTEGER NOT NULL,
  distrito_id INTEGER NOT NULL,
  FOREIGN KEY (distrito_id) REFERENCES distritos (id)
);

-- migrate:down
DROP TABLE codigo_postal;
