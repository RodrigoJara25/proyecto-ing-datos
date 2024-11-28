-- migrate:up
CREATE TABLE ofertas_laborales_condiciones (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

  oferta_laboral_id INTEGER NOT NULL,
  condicion_id INTEGER NOT NULL,
  
  FOREIGN KEY (oferta_laboral_id) REFERENCES ofertas_laborales (id),
  FOREIGN KEY (condicion_id) REFERENCES condiciones (id)
  
);

-- migrate:down
DROP TABLE ofertas_laborales_condiciones;
