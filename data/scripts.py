from faker import Faker
from datetime import datetime

import random


# Crea una instancia de Faker
fake = Faker()      # Faker fake = new Faker();


def llenar_producto():
    i = 1
    contenido = ''
    # Abre el archivo CSV
    with open('productos.txt', mode='r', encoding='utf-8') as archivo:
        # Itera sobre las filas y las imprime
        for fila in archivo:
            fila = fila.strip().split("::")    # para eliminar el espaciado entre lineas usamos .strip()   y para divir en una lista usamos .split("::")
            id = fila[0]
            nombre = fila[1].capitalize()       # capitalize() para ponerle mayusucla a cada nombre
            categoria_id = fila[2]
            descripcion = fake.paragraph()     # fake.paragraph() para generar texto random
            codigo = random.randint(1000,5000)
            valor_unitario = random.randint(5,200)/100.0
            tmp = f"INSERT INTO productos (id, nombre, codigo, descripcion, valor_unitario, categoria_id) VALUES ({id}, '{nombre}', {codigo}, '{descripcion}', {valor_unitario}, {categoria_id});\n"
            contenido = contenido + tmp
            
    # Crear o abrir el archivo en modo escritura
    with open("inserts_productos.sql", "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def llenar_clientes():
    i = 0
    contenido = ''
    while i < 100:
        id = i + 1
        nombre = fake.name()
        direccion = fake.address()
        rif = random.randint(10000000, 99999999)
        ciudad_id = random.randint(1, 4)
        tmp = f"INSERT INTO clientes (id, nombre, direccion, rif, ciudad_id) VALUES ({id}, '{nombre}', '{direccion}', {rif}, {ciudad_id});\n"
        contenido = contenido + tmp 
        i = i + 1
    with open('insert_clientes.sql', 'w', encoding = 'utf-8') as archivo:
        archivo.write(contenido)


def llenar_facturas():
    i = 0
    contenido = ''
    fecha_inicio = datetime(2022,1,1)
    fecha_fin = datetime(2023,12,13)
    while i < 1000:
        id = i + 1
        numero = 100000 + id
        cliente_id = random.randint(1,100)
        fecha_aleatoria = fake.date_time_between(start_date=fecha_inicio, end_date=fecha_fin)
        fecha = fecha_aleatoria.strftime('%Y-%m-%d %H:%M:%S')
        tmp = f"INSERT INTO facturas (id, numero, fecha, cliente_id) VALUES ({id}, {numero}, '{str(fecha)}', {cliente_id});\n"
        contenido = contenido + tmp 
        i = i + 1
    with open('insert_facturas.sql', 'w', encoding = 'utf-8') as archivo:
        archivo.write(contenido)

def llenar_experiencias():
    contenido = ''
    i = 0
    while i < 200:
        tiempo = random.randint(0, 5)
        descripcion = fake.paragraph()
        id = i + 1
        tmp = f"INSERT INTO experiencias (id, tiempo, descripcion) VALUES ({id}, {tiempo}, '{descripcion}');\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_experiencias.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_codigo_postal():
    contenido = ''
    i = 0
    lista_numeros_generados = []
    while i < 50:
        numero = random.randint(10000, 99999)
        if numero not in lista_numeros_generados:
            lista_numeros_generados.append(numero)
            distrito_id = i + 1
            id = i + 1
            tmp = f"INSERT INTO codigo_postal (id, numero, distrito_id) VALUES ({id}, {numero}, {distrito_id});\n"
            contenido = contenido + tmp
            i = i + 1
    with open('inserts_codigo_postal.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_postulantes():
    contenido = ''
    i = 0
    while i < 200:
        id = i + 1
        nombre = fake.first_name()
        experiencia = fake.paragraph()
        perfil = fake.paragraph()
        correo = fake.email()
        sitio_web = fake.url()
        cv = fake.url()
        carrera_profesional_id = random.randint(1, 12)
        condicion_id = random.randint(1,9)
        if 3 <= condicion_id:
            ciclo_id = condicion_id + 1
        else:
            ciclo_id = 10
        tmp = f"INSERT INTO postulantes (id, nombre, experencia, perfil, correo, sitio_web, cv, carrera_profesional_id, condicion_id, ciclo_id) VALUES ({id}, '{nombre}', '{experiencia}', '{perfil}', '{correo}', '{sitio_web}', '{cv}', {carrera_profesional_id}, {condicion_id}, {ciclo_id});\n"
        contenido = contenido + tmp
        i = i + 1

    with open('inserts_postulantes.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_proyectos():
    contenido = ''
    i = 0
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    years = [2020, 2021, 2022, 2023, 2024]
    while i < 200:
        id = i + 1
        titulo = fake.sentence()
        descripcion = fake.paragraph()
        n_random = random.randint(0, 11)
        mes_inicio = meses[n_random]
        n_random = random.randint(0, 11)
        mes_final = meses[n_random]
        n_random = random.randint(0, 4)
        anio_inicio = years[n_random]
        n_random = random.randint(0, 4)
        anio_final = years[n_random]
        postulante_id = random.randint(1, 200)
        tipos_proyecto_id = random.randint(1, 3)
        tmp = f"INSERT INTO proyectos (id, titulo, descripcion, mes_inicio, mes_final, anio_inicio, anio_final, postulante_id, tipos_proyecto_id) VALUES ({id}, '{titulo}', '{descripcion}', '{mes_inicio}', '{mes_final}', {anio_inicio}, {anio_final}, {postulante_id}, {tipos_proyecto_id});\n"
        contenido = contenido + tmp
        i = i + 1
    
    with open('inserts_proyectos.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_empresas():
    contenido = ''
    i = 1
    with open('nombres_empresas.txt', mode='r', encoding='utf-8') as archivo:
        # Itera sobre las filas (son 50 empresas)
        for fila in archivo:
            id = i 
            nombre = fila.strip()
            cantidad_empleados = random.randint(1, 10)
            contacto = fake.url()
            informacion_general = fake.paragraph()
            industria_id = random.randint(1, 20)
            tipo_empresa_id = random.randint(1, 4)
            tmp = f"INSERT INTO empresas (id, nombre, cantidad_empleados, contacto, informacion_general, industria_id, tipo_empresa_id) VALUES ({id}, '{nombre}', {cantidad_empleados}, '{contacto}', '{informacion_general}', {industria_id}, {tipo_empresa_id});\n"
            contenido = contenido + tmp
            i = i + 1

    with open('inserts_empresas.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)



# llenar_producto()
# llenar_clientes()
# llenar_facturas()

# llenar_experiencias()
# llenar_codigo_postal()
# llenar_postulantes()
# llenar_proyectos()
llenar_empresas()