-- migrate:up
CREATE TABLE ofertas_laborales_carreras_profesionales (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

  oferta_laboral_id INTEGER NOT NULL,
  carrera_profesional_id INTEGER NOT NULL,
  
  FOREIGN KEY (oferta_laboral_id) REFERENCES ofertas_laborales (id),
  FOREIGN KEY (carrera_profesional_id) REFERENCES carreras_profesionales (id)
  
);

-- migrate:down
DROP TABLE ofertas_laborales_carreras_profesionales;
