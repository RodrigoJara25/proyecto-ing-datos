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
        <h2>Agregar Carrera</h2>
        <a href = "/consultar_tablas">Retroceder</a>

        <form action = "/carrera/create" method = "post">
            <label>Nombre</>
            <input type = "text" name = "nombre"><br>
            <input type = "submit" value = "Enviar">
        </form>
        
    </div>

    <footer>
        <p>&copy; 2024 Mi Página de Inicio. Todos los derechos reservados.</p>
    </footer>
</body>
</html>