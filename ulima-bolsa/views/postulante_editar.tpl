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
        <h1>Sistema de Gestión de Base de Datos de Bolsa de Trabajo</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/usuarios">Pagina de Usuario</a>
            <a href="/empresas">Pagina de Empresa</a>
        </nav>
    </header>

    <div class="content">
        <h2>Editar Postulante</h2>
        <a href = "/usuarios">Retroceder</a>

        <form action = "/postulante/edit" method = "post">
            <input type = "hidden" name = "id" value = "{{postulantes['id']}}"><br>
            <label>Nombre</>
            <input type = "text" name = "name" value = "{{postulantes['Nombre']}}"><br>
            <label>Experiencia</>
            <input type = "text" name = "experiencia" value = "{{postulantes['Experencia']}}"><br>
            <label>Perfil</>
            <input type = "text" name = "perfil" value = "{{postulantes['Perfil']}}"><br>
            <label>Correo</>
            <input type = "text" name = "correo" value = "{{postulantes['Correo']}}"><br>
            <label>Carrera Profesional</>
            % for c in carreras:
                % if c['id'] == postulantes['carrera_profesional_id']:
                    <span>{{c['Nombre']}}</span> <!-- Muestra el nombre de la carrea -->
                % end
            % end
            <select name="carrera_profesional_id">
            % for c in carreras:
              <option value="{{c['id']}}"> {{c['Nombre']}}</option>
            % end
            </select>
            <br>
            <label>Condicion</>
            % for c in condiciones:
                % if c['id'] == postulantes['condicion_id']:
                    <span>{{c['nombre']}}</span> <!-- Muestra el nombre de la condicion -->
                % end
            % end
            <select name="condicion_id">
            % for c in condiciones:
              <option value="{{c['id']}}"> {{c['Nombre']}}</option>
            % end
            </select>
            <br>
            <label>Ciclo</>
            % for c in ciclos:
                % if c['id'] == postulantes['ciclo_id']:
                    <span>{{c['ciclo']}}</span> <!-- Muestra el nombre del ciclo -->
                % end
            % end
            <select name="ciclo_id">
            % for c in ciclos:
              <option value="{{c['id']}}"> {{c['ciclo']}}</option>
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