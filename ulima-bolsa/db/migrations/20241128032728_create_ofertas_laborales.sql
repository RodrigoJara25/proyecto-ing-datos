-- migrate:up
CREATE TABLE ofertas_laborales (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

  conocimientos VARCHAR(200) NOT NULL,
  numero_vacantes INTEGER NOT NULL,
  codigo_oferta INTEGER NOT NULL,
  nombre_puesto VARCHAR(80) NOT NULL,
  habilidades VARCHAR(200) NOT NULL,
  fecha_publicacion DATE NOT NULL,
  fecha_limite_postulacion DATE NOT NULL,
  horario_trabajo VARCHAR(200) NOT NULL,
  beneficios_adicionales VARCHAR(200) NOT NULL,
  descripcion_funciones VARCHAR(200) NOT NULL,
  informacion_adicional VARCHAR(200) NOT NULL,

  disponibilidad_horario_id INTEGER NOT NULL,
  modalidad_id INTEGER NOT NULL,
  empresa_id INTEGER NOT NULL,
  experiencia_id INTEGER NOT NULL,
  tipo_oferta_id INTEGER NOT NULL,
  distrito_id INTEGER NOT NULL,
  FOREIGN KEY (disponibilidad_horario_id) REFERENCES disponibilidad_horarioS (id),
  FOREIGN KEY (modalidad_id) REFERENCES modalidades (id),
  FOREIGN KEY (empresa_id) REFERENCES empresas (id),
  FOREIGN KEY (experiencia_id) REFERENCES experiencias (id),
  FOREIGN KEY (tipo_oferta_id) REFERENCES tipos_ofertas (id),
  FOREIGN KEY (distrito_id) REFERENCES distritos (id)
);

-- migrate:down
DROP TABLE ofertas_laborales;
