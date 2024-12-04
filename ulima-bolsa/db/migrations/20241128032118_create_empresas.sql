-- migrate:up
CREATE TABLE empresas (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(40) NOT NULL,
  cantidad_empleados INTEGER NOT NULL,
  contacto VARCHAR(50) NOT NULL,
  informacion_general VARCHAR(200) NOT NULL,

  industria_id INTEGER NOT NULL,
  tipo_empresa_id INTEGER NOT NULL,
  FOREIGN KEY (industria_id) REFERENCES industrias (id),
  FOREIGN KEY (tipo_empresa_id) REFERENCES tipos_empresas (id)
);

-- migrate:down
DROP TABLE empresas;
