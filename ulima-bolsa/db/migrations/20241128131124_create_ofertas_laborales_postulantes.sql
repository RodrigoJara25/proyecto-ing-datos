-- migrate:up
CREATE TABLE ofertas_laborales_postulantes (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

  oferta_laboral_id INTEGER NOT NULL,
  postulante_id INTEGER NOT NULL,
  
  FOREIGN KEY (oferta_laboral_id) REFERENCES ofertas_laborales (id),
  FOREIGN KEY (postulante_id) REFERENCES postulantes (id)
  
);

-- migrate:down
DROP TABLE ofertas_laborales_postulantes;
