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
        <h2>Tu puente hacia nuevas oportunidades laborales</h2>
        <p>
          Publica ofertas laborales o postúlate a trabajos desde cualquier lugar. ¡Da el siguiente paso en tu carrera!
        </p>

        <br>
        <div>
            <h3>FILTROS</h3>
            <form action="/ofertas/buscar_empresa" method="get"> <!-- Agrega el atributo action -->
                <label>Busca la empresa:</label>
                <input type="text" name="nombre" value="PepsiCo"> <!-- Especifica un nombre para el campo -->
                <input type="submit" value="Buscar">
            </form>
            <form action="/ofertas/buscar_modalidad" method="get"> <!-- Agrega el atributo action -->
                <label>Busca la modalidad:</label>
                <input type="text" name="name_modalidad" value="Presencial"> <!-- Especifica un nombre para el campo -->
                <input type="submit" value="Buscar">
            </form>
            <form action="/ofertas/buscar_tipo_oferta" method="get"> <!-- Agrega el atributo action -->
                <label>Busca el tipo de oferta:</label>
                <input type="text" name="name_tipo" value="Practicas"> <!-- Especifica un nombre para el campo -->
                <input type="submit" value="Buscar">
            </form>
        </div>
        <br>
        <br>
        <table>
            <thead>
                <th>Puesto <br> <a href = "/ofertas/ordenar_puesto"> Ordenar por Puesto </a></th>
                <th>Vacantes <br> <a href = "/ofertas/ordenar_vacantes"> Ordenar por Vacantes </a></th>
                <th>Empresa <br> <a href = "/ofertas/ordenar_empresa"> Ordenar por Empresa </a></th>
                <th>Modalidad <br> <a href = "/ofertas/ordenar_modalidad"> Ordenar por Modalidad </a></th>
                <th>Tipo de oferta <br> <a href = "/ofertas/ordenar_tipo_oferta"> Ordenar por Tipo de Oferta </a></th>
            </thead>
            <tbody>
                % for oferta in ofertas:
                <tr>
                    <td>{{oferta['Puesto']}}</td>
                    <td>{{oferta['Vacantes']}}</td>
                    <td>{{oferta['Empresa']}}</td>
                    <td>{{oferta['Modalidad']}}</td>
                    <td>{{oferta['Tipo de oferta']}}</td>
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