from bottle import route, run, template, static_file, request, redirect
from configs.database import Database  #importamos la clase "Database"
import os

# para usar los archvios dentro de la carpeta "static" (css, imagenes, etc) y
# para usar la carpeta "static" sin tener que usar todo el rato ./static
@route('/<filename>')
def server_static(filename):
  return static_file(filename, root='./static')


# decoratiors: son como envoltorios que envuelven a la funcion
# es de la libreria bottle
@route('/')
def home():
  db = Database()
  query = (f"""SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
                      
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/ordenar_puesto')
def ofertas_ordenar_puesto():
  db = Database()
  query = (f"""
            SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
              
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id

            ORDER BY ofertas_laborales.nombre_puesto ASC;
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/ordenar_vacantes')
def ofertas_ordenar_vacantes():
  db = Database()
  query = (f"""
            SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
              
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id

            ORDER BY ofertas_laborales.numero_vacantes DESC;
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/ordenar_empresa')
def ofertas_ordenar_empresa():
  db = Database()
  query = (f"""
            SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
              
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id

            ORDER BY empresas.nombre ASC;
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/ordenar_modalidad')
def ofertas_ordenar_modalidad():
  db = Database()
  query = (f"""
            SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
              
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id

            ORDER BY modalidades.nombre ASC;
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/ordenar_tipo_oferta')
def ofertas_ordenar_tipo_oferta():
  db = Database()
  query = (f"""
            SELECT 
              ofertas_laborales.id,
              ofertas_laborales.nombre_puesto AS 'Puesto',
              ofertas_laborales.numero_vacantes AS 'Vacantes',
              empresas.nombre AS 'Empresa',
              modalidades.nombre AS 'Modalidad',
              tipos_ofertas.nombre AS 'Tipo de oferta'
              
            FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
                INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id

            ORDER BY tipos_ofertas.nombre ASC;
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('index', ofertas=rs)

@route('/ofertas/buscar_empresa', method='GET')
def ofertas_buscar_empresa():
    db = Database()
    # Obtener el nombre del Pokémon del formulario
    nombre = request.query.nombre  # Asegúrate de que este sea el nombre del campo en tu formulario
    # Realizar la consulta para buscar el Pokémon por nombre
    query = (f"""
      SELECT 
        ofertas_laborales.id,
        ofertas_laborales.nombre_puesto AS 'Puesto',
        ofertas_laborales.numero_vacantes AS 'Vacantes',
        empresas.nombre AS 'Empresa',
        modalidades.nombre AS 'Modalidad',
        tipos_ofertas.nombre AS 'Tipo de oferta'
    
      FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
          INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
          INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id
    
      WHERE empresas.nombre LIKE '%{nombre}%'
    """)
    rs = db.fetchall(query)
    db.close()  # Cierra la conexión a la base de datos
    return template('index', ofertas=rs)

@route('/ofertas/buscar_modalidad', method='GET')
def ofertas_buscar_modalidad():
    db = Database()
    # Obtener el nombre del Pokémon del formulario
    nombre = request.query.name_modalidad  # Asegúrate de que este sea el nombre del campo en tu formulario
    # Realizar la consulta para buscar el Pokémon por nombre
    query = (f"""
      SELECT 
        ofertas_laborales.id,
        ofertas_laborales.nombre_puesto AS 'Puesto',
        ofertas_laborales.numero_vacantes AS 'Vacantes',
        empresas.nombre AS 'Empresa',
        modalidades.nombre AS 'Modalidad',
        tipos_ofertas.nombre AS 'Tipo de oferta'
    
      FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
          INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
          INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id
    
      WHERE modalidades.nombre LIKE '%{nombre}%'
    """)
    rs = db.fetchall(query)
    db.close()  # Cierra la conexión a la base de datos
    return template('index', ofertas=rs)

@route('/ofertas/buscar_tipo_oferta', method='GET')
def ofertas_buscar_tipo_oferta():
    db = Database()
    # Obtener el nombre del Pokémon del formulario
    nombre = request.query.name_tipo  # Asegúrate de que este sea el nombre del campo en tu formulario
    # Realizar la consulta para buscar el Pokémon por nombre
    query = (f"""
      SELECT 
        ofertas_laborales.id,
        ofertas_laborales.nombre_puesto AS 'Puesto',
        ofertas_laborales.numero_vacantes AS 'Vacantes',
        empresas.nombre AS 'Empresa',
        modalidades.nombre AS 'Modalidad',
        tipos_ofertas.nombre AS 'Tipo de oferta'
    
      FROM ofertas_laborales INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
          INNER JOIN modalidades ON ofertas_laborales.modalidad_id = modalidades.id
          INNER JOIN tipos_ofertas ON ofertas_laborales.tipo_oferta_id = tipos_ofertas.id
    
      WHERE tipos_ofertas.nombre LIKE '%{nombre}%'
    """)
    rs = db.fetchall(query)
    db.close()  # Cierra la conexión a la base de datos
    return template('index', ofertas=rs)

@route('/usuarios')
def usuarios():
  db = Database()
  query = (f"""
          SELECT
            postulantes.id,
            postulantes.nombre AS 'Nombre',
            postulantes.experencia AS 'Experiencia',
            postulantes.perfil AS 'Perfil',
            postulantes.correo AS 'Correo',
            carreras_profesionales.nombre AS 'Carrera Profesional',
            condiciones.nombre AS 'Condicion',
            ciclos.ciclo AS 'Ciclo'
          FROM postulantes INNER JOIN carreras_profesionales ON postulantes.carrera_profesional_id = carreras_profesionales.id
                  INNER JOIN condiciones ON postulantes.condicion_id = condiciones.id
                  INNER JOIN ciclos ON postulantes.ciclo_id = ciclos.id
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('usuarios', ofertas=rs)

@route('/consultar_tablas', method='POST')
def consultar_tablas():
  # Obtener los datos del formulario
  tabla = request.forms.get('opcion')
  if tabla == 'opcion1':
      db = Database()
      query = (f"""
              SELECT
                *
              FROM carreras_profesionales
                  """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('carreras', ofertas=rs)
  elif tabla == 'opcion2':
      db = Database()
      query = (f"""
              SELECT
                *
              FROM condiciones
                  """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('condiciones', ofertas=rs)
  elif tabla == 'opcion3':
      db = Database()
      query = (f"""
              SELECT
                *
              FROM ciclos
                  """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('ciclos', ofertas=rs)

@route('/postulante/editar', method='GET')
def editar_postulante():
  # Obtener los datos del formulario
  postulante_id = request.query.id
  # acceder a la base de datos
  db = Database()
  # info pokemon
  query = (f"SELECT * FROM postulantes WHERE id = {postulante_id};")
  postulante = db.fetchone(query)
  
  query_carrera = ("SELECT * FROM carreras_profesionales;")
  carrera = db.fetchall(query_carrera)

  query_condicion = ("SELECT * FROM condiciones;")
  condicion = db.fetchall(query_condicion)

  query_ciclo = ("SELECT * FROM ciclos;")
  ciclo = db.fetchall(query_ciclo)

  db.close()
  # ir al inicio
  return template('postulante_editar', postulantes=postulante, carreras=carrera, condiciones=condicion, ciclos=ciclo)

@route('/postulante/edit', method='POST')
def edit_postulante():
  # Obtener los datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('name')
  experencia = request.forms.get('experiencia')
  perfil = request.forms.get('perfil')
  correo = request.forms.get('correo')
  carrera_profesional_id = request.forms.get('carrera_profesional_id')
  condicion_id = request.forms.get('condicion_id')
  ciclo_id = request.forms.get('ciclo_id')
  # acceder a la base de datos
  db = Database()
  query = (
      f"UPDATE postulantes SET nombre = '{nombre}', experencia = '{experencia}', perfil = '{perfil}',"
      f" correo = '{correo}', carrera_profesional_id = {carrera_profesional_id}, condicion_id = {condicion_id}, ciclo_id = {ciclo_id}"
      f" WHERE id = {id}"
  )
  print(query)
  db.execute(query)
  db.close()
  # ir al inicio
  return redirect('/usuarios')

@route('/postulante/eliminar', method = 'GET')
def eliminar_postulante():
  postulante_id = request.query.id
  db = Database()
  query = (f"DELETE FROM postulantes WHERE id = {postulante_id};")
  db.execute(query)
  db.close()
  return redirect('/usuarios')

@route('/carrera/agregar')
def carrera_agregar():
  return template('carrera_agregar')

@route('/carrera/create', method='POST')
def create_carrera():
  # Obtener los datos del formulario
  nombre = request.forms.get('nombre')
  # acceder a la base de datos
  db = Database()
  query = (
      f"INSERT INTO carreras_profesionales (nombre) "
      f"VALUES ('{nombre}')"
  )
  db.execute(query)
  db.close()
  # ir al inicio
  return redirect('/usuarios')

@route('/carrera/eliminar', method = 'GET')
def eliminar_carrera():
  carrera_id = request.query.id
  db = Database()
  query = (f"DELETE FROM carreras_profesionales WHERE id = {carrera_id};")
  db.execute(query)
  db.close()
  return redirect('/usuarios')

@route('/empresas')
def empresas():
  db = Database()
  query = (f"""
          SELECT
            empresas.nombre AS 'Nombre',
            empresas.cantidad_empleados AS 'Empleados',
            empresas.contacto AS 'Contacto',
            empresas.informacion_general AS 'Informacion',
            industrias.nombre AS 'Industria',
            tipos_empresas.nombre AS 'Tipo'
          FROM empresas INNER JOIN industrias ON empresas.industria_id = industrias.id
                INNER JOIN tipos_empresas ON empresas.tipo_empresa_id = tipos_empresas.id
              """)  # le respuesta de la consulta la almacenamos (la tabla)
  rs = db.fetchall(query)
  return template('empresas', ofertas=rs)

@route('/consultar_tablas_empresas', method='POST')
def consultar_tablas_empresas():
  # Obtener los datos del formulario
  tabla = request.forms.get('opcion')
  if tabla == 'opcion1':
      db = Database()
      query = (f"""
              SELECT
                ofertas_laborales.id AS 'OfertaID',
                ofertas_laborales.nombre_puesto AS 'Puesto',
                empresas.nombre AS 'Empresa',
                postulantes.nombre AS 'Postulante',
                postulantes.id AS 'PostulanteID'
              FROM ofertas_laborales_postulantes INNER JOIN ofertas_laborales ON ofertas_laborales_postulantes.oferta_laboral_id = ofertas_laborales.id
                                INNER JOIN postulantes ON ofertas_laborales_postulantes.postulante_id = postulantes.id
                                INNER JOIN empresas ON ofertas_laborales.empresa_id = empresas.id
                  """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('ofertas_laborales_postulantes', ofertas=rs)
  elif tabla == 'opcion2':
      db = Database()
      query = (f"""
              SELECT
                ofertas_laborales.id AS 'OfertaID',
                ofertas_laborales.nombre_puesto AS 'Puesto',
                condiciones.nombre AS 'Condicion'
              FROM ofertas_laborales_condiciones INNER JOIN condiciones ON ofertas_laborales_condiciones.condicion_id = condiciones.id
                              INNER JOIN ofertas_laborales ON ofertas_laborales_condiciones.oferta_laboral_id = ofertas_laborales.id
                """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('ofertas_laborales_condiciones', ofertas=rs)
  elif tabla == 'opcion3':
      db = Database()
      query = (f"""
              SELECT
                ofertas_laborales.id AS 'OfertaID',
                ofertas_laborales.nombre_puesto AS 'Puesto',
                carreras_profesionales.nombre AS 'Carrera'
              FROM ofertas_laborales_carreras_profesionales INNER JOIN carreras_profesionales ON ofertas_laborales_carreras_profesionales.carrera_profesional_id = carreras_profesionales.id
                              INNER JOIN ofertas_laborales ON ofertas_laborales_carreras_profesionales.oferta_laboral_id = ofertas_laborales.id
              """)  # le respuesta de la consulta la almacenamos (la tabla)
      rs = db.fetchall(query)
      return template('ofertas_laborales_carreras_profesionales', ofertas=rs)

# esta es la funcion main
# a su vez ejecuta una funcion "run" de una libreria
# if __name__ == '__main__':
#   run(host='localhost', port=8080, reloader=True)

  # Obtén el puerto desde la variable de entorno de Render (si está disponible), o usa 8080 como predeterminado.
port = int(os.environ.get("PORT", 8080))

# Corre el servidor de Bottle, asegurándote de escuchar en todas las interfaces.
if __name__ == '__main__':
  run(host='0.0.0.0', port=port, reloader=True)
