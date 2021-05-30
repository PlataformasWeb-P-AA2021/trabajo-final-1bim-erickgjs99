import itertools
from itertools import chain
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Canton, Provincia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

"""
Para abrir los archivos de instituciones educativas
"""
openCsv = open('data/Listado-Instituciones-Educativas.csv',
               'r', encoding='utf-8')

# Varible auxiliar para almacenar los cantones
cantonesAux = []

"""
Ciclo repetitivo for para que lea nuestro archivo,
con la declaración le decimos que lea a partir de la primer
elemento de nuestro ciclo for, dejando las filas que tienen
el nombre de la propiedad
"""
for i in itertools.islice(openCsv, 1, None):
    """
    En la linea 39 - 40 - 41 separamos todos elementos dentro
    el conjunto de datos separandolos por el | y el /n, 
    primero separando los elementos por el | y luego, recorriendo
    en reversa la lista para eliminar el salto de linea 
    """
    texto = i.split("|")
    texto_final = texto[len(texto)-1].split("\n")
    texto[len(texto)-1] = texto_final[0]
    # almacenamos todo en una lista auxiliar
    cantonesAux.append((texto[4], texto[5], texto[2]))

# guardamos los valores unicos de la lista auxiliar
cantonesAux = list(set(tuple(cantonesAux)))
# hacemos una consulta para sacar todos los cantones
provincias = session.query(Provincia).all()

# Ciclo for para guardar los datos
for i in cantonesAux:
    for j in provincias:
        # Comparamos si el nombre de la provincia coincide con la consulta
        # empleada
        if(i[2] == j.provincia):
            # Guardamos el codigo de canton en la posición 4 de la lista
            i[4] = j.codigo
    # Lo guardamos el objeto Canton
    ingresaCan = Canton(codigo=i[0], canton=i[1], provincia_id=i[2])
    # Lo agregamos a la base de datos
    session.add(ingresaCan)
# Confirmamos lo cambios
session.commit()
