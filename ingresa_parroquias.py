import itertools
from itertools import chain
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Parroquia, Canton

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

parrAux = []

"""
Ciclo repetitivo for para que lea nuestro archivo,
con la declaración le decimos que lea a partir de la primer
elemento de nuestro ciclo for, dejando las filas que tienen
el nombre de la propiedad
"""
for i in itertools.islice(openCsv, 1, None):
    """
    En las siguientes lineas separamos todos elementos dentro
    el conjunto de datos separandolos por el | y el /n, 
    primero separando los elementos por el | y luego, recorriendo
    en reversa la lista para eliminar el salto de linea 
    """
    texto = i.split("|")
    texto_final = texto[len(texto)-1].split("\n")
    texto[len(texto)-1] = texto_final[0]

    # almacenamos todo en una lista auxiliar
    parrAux.append((texto[6], texto[7], texto[4]))

# guardamos los valores unicos de la lista auxiliar
parrAux = list(set(tuple(parrAux)))

# hacemos una consulta para sacar todos los valores de Canton
cantones = session.query(Canton).all()
# Ciclo for para guardar los datos
for i in parrAux:
    for j in cantones:
        # Comparamos si el nombre de canton coincide
        if(i[2] == j.canton):
            # Se guarda el codigo de canton en la posicion 4
            i[4] = j.codigo
    # Lo guardamos el objeto Parroquia
    ingresaParr = Parroquia(codigo=i[0], parroquia=i[1], canton_id=i[2])
    # Guardamos en la base de datos
    session.add(ingresaParr)

# Confirmamos las transicciones
session.commit()
