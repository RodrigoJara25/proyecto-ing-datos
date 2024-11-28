-- migrate:up
CREATE TABLE proyectos (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  titulo VARCHAR(50) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  mes_inicio VARCHAR(30),
  mes_final VARCHAR(30),
  anio_inicio INTEGER NOT NULL,
  anio_final INTEGER NOT NULL,
  postulante_id INTEGER NOT NULL,
  tipos_proyecto_id INTEGER NOT NULL,
  FOREIGN KEY (postulante_id) REFERENCES postulantes (id),
  FOREIGN KEY (tipos_proyecto_id) REFERENCES tipos_proyectos (id)
);

-- migrate:down
DROP TABLE proyectos;
