<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página de Inicio</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <h1>Index</h1>
        <nav>
            <a href="#">Inicio</a>
            <a href="/nosotros">Nosotros</a>
            <a href="/usuarios">Usuarios</a>
            <a href="/servicios">Servicios</a>
            <a href="/contacto">Contacto</a>
        </nav>
    </header>

    <div class="content">
        <h2>Editar Pokemon</h2>
        <a href = "/">Retroceder</a>

        <form action = "/pokemon/edit" method = "post">
            <input type = "hidden" name = "id" value = "{{pokemon['id']}}"><br>
            <label>Nombre</>
            <input type = "text" name = "name" value = "{{pokemon['name']}}"><br>
            <label>Pokedex</>
            <input type = "text" name = "number" value = "{{pokemon['number']}}"><br>
            <label>Peso</>
            <input type = "text" name = "weight" value = "{{pokemon['weight']}}"><br>
            <label>Estatura</>
            <input type = "text" name = "height" value = "{{pokemon['height']}}"><br>
            <label>Imagen</>
            <input type = "text" name = "image_url" value = "{{pokemon['image_url']}}"><br>
            <label>Generacion</>
            % for g in generations:
                % if g['id'] == pokemon['generation_id']:
                    <span>{{g['name']}}</span> <!-- Muestra el nombre de la generación -->
                % end
            % end
            <select name="generation_id">
            % for g in generations:
              <option value="{{g['id']}}"> {{g['name']}}</option>
            % end
            </select>
            <input type = "submit" value = "Enviar">
        </form>

    </div>

    <footer>
        <p>&copy; 2024 Mi Página de Inicio. Todos los derechos reservados.</p>
    </footer>
</body>
</html>