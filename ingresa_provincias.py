import itertools
from itertools import chain
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Provincia

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

provaux = []
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
    provaux.append((texto[2], texto[3]))

# guardamos los valores unicos de la lista auxiliar
provaux = list(set(tuple(provaux)))


# Ciclo for para guardar los datos
for i in provaux:
    # Lo guardamos el objeto Provincia
    ingresaProv = Provincia(codigo=i[0], provincia=i[1])
    # Los agregamos a la base de datos
    session.add(ingresaProv)
# Confirmamos lo cambios
session.commit()
