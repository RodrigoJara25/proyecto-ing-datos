-- migrate:up
CREATE TABLE ofertas_laborales_idiomas (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

  oferta_laboral_id INTEGER NOT NULL,
  idioma_id INTEGER NOT NULL,
  
  FOREIGN KEY (oferta_laboral_id) REFERENCES ofertas_laborales (id),
  FOREIGN KEY (idioma_id) REFERENCES idiomas (id)
  
);

-- migrate:down
DROP TABLE ofertas_laborales_idiomas;
