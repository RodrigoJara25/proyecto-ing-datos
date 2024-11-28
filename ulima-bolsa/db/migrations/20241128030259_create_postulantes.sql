-- migrate:up
CREATE TABLE postulantes (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL,
  experencia VARCHAR(200) NOT NULL,
  perfil VARCHAR(200),
  correo VARCHAR(20),
  sitio_web VARCHAR(50),
  cv VARCHAR(50),
  carrera_profesional_id INTEGER NOT NULL,
  condicion_id INTEGER NOT NULL,
  ciclo_id INTEGER NOT NULL,
  FOREIGN KEY (ciclo_id) REFERENCES ciclos (id),
  FOREIGN KEY (carrera_profesional_id) REFERENCES carreras_profesionales (id),
  FOREIGN KEY (condicion_id) REFERENCES condiciones (id)
);

-- migrate:down
DROP TABLE postulantes;
