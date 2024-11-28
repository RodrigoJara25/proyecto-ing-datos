-- migrate:up
CREATE TABLE ofertas_laborales (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  conocimiento VARCHAR(200) NOT NULL,
  numeros_vacantes INTEGER NOT NULL,
  codigo_oferta INTEGER NOT NULL,
  nombre_puesto VARCHAR(80) NOT NULL,
  habilidades VARCHAR(200),
  fecha_publicacion DATE NOT NULL,
  fecha_limite_postulacion DATE NOT NULL,
  horario_trabajo VARCHAR(200),
  beneficios_adicionales VARCHAR(200),
  descripcion_funciones VARCHAR(200),
  informacion_adicional VARCHAR(200),

  disponibilidad_horario_id INTEGER NOT NULL,
  modalidad_id INTEGER NOT NULL, 

  FOREIGN KEY (disponibilidad_horario_id) REFERENCES disponibilidad_horarios (id),
  FOREIGN KEY (modalidad_id) REFERENCES modalidades (id),



  cantidad_empleados INTEGER NOT NULL,
  contacto VARCHAR(50) NOT NULL,
  informacion_general VARCHAR(200) NOT NULL,

  industria_id INTEGER NOT NULL,
  tipo_empresa_id INTEGER NOT NULL,
  FOREIGN KEY (industria_id) REFERENCES industrias (id),
  FOREIGN KEY (tipo_empresa_id) REFERENCES tipos_empresas (id)
);

-- migrate:down
DROP TABLE ofertas_laborales;
