from faker import Faker
from datetime import datetime

import random

# Crea una instancia de Faker
fake = Faker()      # Faker fake = new Faker();


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

def llenar_ofertas_laborales():
    contenido = ''
    i = 0
    lista_random = []
    while i < 200:
        id = i + 1
        conocimientos = fake.paragraph()
        numero_vacantes = random.randint(1, 5)
        codigo_oferta = random.randint(1000, 1500)
        nombre_puesto = fake.job()
        habilidades = fake.paragraph()
        fecha_publicacion =  fake.date_between(start_date="-1y", end_date="today")
        fecha_limite_postulacion = fake.date_between(start_date="-1y", end_date="today")
        horario_trabajo = fake.paragraph()
        beneficios_adicionales = fake.paragraph()
        descripcion_funciones = fake.paragraph()
        informacion_adicional = fake.paragraph()
        disponibilidad_horario_id = random.randint(1, 2)
        modalidad_id = random.randint(1, 3)
        empresa_id = random.randint(1, 50)
        experiencia_id = random.randint(1, 50)
        tipo_oferta_id = random.randint(1, 3)
        distrito_id = random.randint(1, 50)
        tmp = f"INSERT INTO ofertas_laborales (id, conocimientos, numero_vacantes, codigo_oferta, nombre_puesto, habilidades, fecha_publicacion, fecha_limite_postulacion, horario_trabajo, beneficios_adicionales, descripcion_funciones, informacion_adicional, disponibilidad_horario_id, modalidad_id, empresa_id, experiencia_id, tipo_oferta_id, distrito_id) VALUES ({id}, '{conocimientos}', {numero_vacantes}, {codigo_oferta}, '{nombre_puesto}', '{habilidades}', '{fecha_publicacion}', '{fecha_limite_postulacion}', '{horario_trabajo}', '{beneficios_adicionales}', '{descripcion_funciones}', '{informacion_adicional}', {disponibilidad_horario_id}, {modalidad_id}, {empresa_id}, {experiencia_id}, {tipo_oferta_id}, {distrito_id});\n"
        contenido = contenido + tmp
        i = i + 1
    
    with open('inserts_ofertas_laborales.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_ofertas_laborales_postulantes():
    contenido = ''
    i = 0
    # Generamos 800 registros en esta relacion de muchos a muchos (asociativa)
    while i < 800:
        id = i + 1
        oferta_laboral_id = random.randint(1, 200)      # elegimos una oferta al azar
        postulante_id = random.randint(1, 200)          # y la vinculamos con un postulante al azar
        tmp = f"INSERT INTO ofertas_laborales_postulantes (id, oferta_laboral_id, postulante_id) VALUES ({id}, {oferta_laboral_id}, {postulante_id});\n"
        contenido = contenido + tmp
        i = i + 1

    with open('inserts_ofertas_laborales_postulantes.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_ofertas_laborales_carreras_profesionales():
    contenido = ''
    i = 0
    # Generamos 200 registros minimo en esta relacion de muchos a muchos (asociativa) para que cada oferta tenga una carrera deseable como minimo
    while i < 200:
        id = i + 1
        oferta_laboral_id = i + 1      # elegimos una oferta 
        carrera_profesional_id = random.randint(1, 12)          # y la vinculamos con una carrera al azar
        tmp = f"INSERT INTO ofertas_laborales_carreras_profesionales (id, oferta_laboral_id, carrera_profesional_id) VALUES ({id}, {oferta_laboral_id}, {carrera_profesional_id});\n"
        contenido = contenido + tmp
        i = i + 1
    j = 0
    # Generamos 400 registros aleaorios para cada oferta y su carrera deseada
    while j < 400:
        id = i + 1
        oferta_laboral_id = random.randint(1, 200)      # elegimos una oferta 
        carrera_profesional_id = random.randint(1, 12)          # y la vinculamos con una carrera al azar
        tmp = f"INSERT INTO ofertas_laborales_carreras_profesionales (id, oferta_laboral_id, carrera_profesional_id) VALUES ({id}, {oferta_laboral_id}, {carrera_profesional_id});\n"
        contenido = contenido + tmp
        i = i + 1
        j = j + 1

    with open('inserts_ofertas_laborales_carreras_profesionales.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

def llenar_ofertas_laborales_condiciones():
    contenido = ''
    i = 0
    # Generamos 200 registros minimo en esta relacion de muchos a muchos (asociativa) para que cada oferta tenga una carrera deseable como minimo
    while i < 200:
        id = i + 1
        oferta_laboral_id = i + 1      # elegimos una oferta 
        condicion_id = random.randint(1, 9)          # y la vinculamos con una condicion al azar
        tmp = f"INSERT INTO ofertas_laborales_condiciones (id, oferta_laboral_id, condicion_id) VALUES ({id}, {oferta_laboral_id}, {condicion_id});\n"
        contenido = contenido + tmp
        i = i + 1
    j = 0
    # Generamos 400 registros aleaorios para cada oferta y su carrera deseada
    while j < 400:
        id = i + 1
        oferta_laboral_id = random.randint(1, 200)      # elegimos una oferta 
        condicion_id = random.randint(1, 9)          # y la vinculamos con una carrera al azar
        tmp = f"INSERT INTO ofertas_laborales_condiciones (id, oferta_laboral_id, condicion_id) VALUES ({id}, {oferta_laboral_id}, {condicion_id});\n"
        contenido = contenido + tmp
        i = i + 1
        j = j + 1

    with open('inserts_ofertas_laborales_condiciones.sql', 'w', encoding = 'utf-8') as file:
        file.write(contenido)

# llenar_experiencias()
# llenar_codigo_postal()
# llenar_postulantes()
# llenar_proyectos()
# llenar_empresas()
# llenar_ofertas_laborales()
# llenar_ofertas_laborales_postulantes()
# llenar_ofertas_laborales_carreras_profesionales()
llenar_ofertas_laborales_condiciones()