from bottle import route, run, template, static_file, request, redirect
from configs.database import Database  #importamos la clase "Database"


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

@route('/pokemon/agregar')
def pokemon_agregar():
  return template('pokemon_agregar')

@route('/pokemon/create', method='POST')
def create_pokemon():
  # Obtener los datos del formulario
  name = request.forms.get('name')
  number = request.forms.get('number')
  weight = request.forms.get('weight')
  height = request.forms.get('height')
  image_url = request.forms.get('image_url')
  generation_id = request.forms.get('generation_id')
  # acceder a la base de datos
  db = Database()
  query = (
      f"INSERT INTO pokemons (name, number, weight, height, image_url, generation_id) "
      f"VALUES ('{name}', {number}, {weight}, {height}, '{image_url}', {generation_id})"
  )
  print(query)
  db.execute(query)
  db.close()
  # ir al inicio
  redirect('https://600e18f4-c523-4a99-9a36-8f6cfafd26f0-00-1yz1dtjeejvub.kirk.replit.dev:8080/')

@route('/pokemon/editar', method='GET')
def editar_pokemon():
  # Obtener los datos del formulario
  pokemon_id = request.query.id
  # acceder a la base de datos
  db = Database()
  # info pokemon
  query = (f"SELECT * FROM pokemons WHERE id = {pokemon_id};")
  pokemon = db.fetchone(query)
  # generaciones
  query2 = ("SELECT * FROM generations;")
  generation = db.fetchall(query2)
  print(pokemon['name'])
  db.close()
  # ir al inicio
  return template('pokemon_editar', pokemon=pokemon, generations=generation)

@route('/pokemon/edit', method='POST')
def edit_pokemon():
  # Obtener los datos del formulario
  id = request.forms.get('id')
  name = request.forms.get('name')
  number = request.forms.get('number')
  weight = request.forms.get('weight')
  height = request.forms.get('height')
  image_url = request.forms.get('image_url')
  generation_id = request.forms.get('generation_id')
  # acceder a la base de datos
  db = Database()
  query = (
      f"UPDATE pokemons SET name = '{name}', number = {number}, weight = {weight},"
      f" height = {height}, image_url = '{image_url}', generation_id = {generation_id}"
      f" WHERE id = {id}"
  )
  print(query)
  db.execute(query)
  db.close()
  # ir al inicio
  return redirect('https://600e18f4-c523-4a99-9a36-8f6cfafd26f0-00-1yz1dtjeejvub.kirk.replit.dev:8080/')

@route('/pokemon/eliminar', method = 'GET')
def eliminar_pokemon():
  pokemon_id = request.query.id
  db = Database()
  query = (f"DELETE FROM pokemons WHERE id = {pokemon_id};")
  db.execute(query)
  db.close()
  return redirect('https://600e18f4-c523-4a99-9a36-8f6cfafd26f0-00-1yz1dtjeejvub.kirk.replit.dev:8080/')

@route('/usuarios2')
def usuarios2():
  db = Database()
  rs = db.fetchall('SELECT * FROM users')
  return template('usuarios', usuarios=rs)


# Con @route podemos crear muchas direcciones
@route('/contacto')
def contacto():
  return template('contacto')


@route('/nosotros')
def nosotros():
  return template('nosotros')


# esta es la funcion main
# a su vez ejecuta una funcion "run" de una libreria
if __name__ == '__main__':
  run(host='localhost', port=8080, reloader=True)
