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
        <h2>Unete a la base de datos de postulantes</h2>
        <p>
          Base de datos de postulantes
        </p>

        <br>
        <div>
            <h3>CONSULTA MAS INFORMACION</h3>
            <form action="/consultar_tablas_empresas" method="POST">
                <p>Consulta otras tablas:</p>
                
                <input type="radio" id="opcion1" name="opcion" value="opcion1">
                <label for="opcion1">Ofertas Laborales Postulantes</label><br>
                
                <input type="radio" id="opcion2" name="opcion" value="opcion2">
                <label for="opcion2">Ofertas Laborales Condiciones</label><br>
                
                <input type="radio" id="opcion3" name="opcion" value="opcion3">
                <label for="opcion3">Ofertas Laborales Carreras Profesionales</label><br>
                <br>
                <button type="submit">Enviar</button>
            </form>
            <br>
            <button onclick="window.location.href='/usuarios';">Regresar a Tabla Empresas</button>

        </div>
        <br>
        <br>
        <table>
            <thead>
                <th>Nombre </th>
                <th>Empleados </th>
                <th>Contacto </th>
                <th>Informacion </th>
                <th>Industria </th>
                <th>Tipo </th>
            </thead>
            <tbody>
                % for oferta in ofertas:
                <tr>
                    <td>{{oferta['Nombre']}}</td>
                    <td>{{oferta['Empleados']}}</td>
                    <td>{{oferta['Contacto']}}</td>
                    <td>{{oferta['Informacion']}}</td>
                    <td>{{oferta['Industria']}}</td>
                    <td>{{oferta['Tipo']}}</td>
                </tr>
                %end
            </tbody>
        </table>
        
    </div>

    <footer>
        <p>&copy; 2024 Rodrigo Jara. Todos los derechos reservados.</p>
    </footer>
</body>
</html>