import itertools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.base import ColumnSet
from sqlalchemy.sql.sqltypes import String

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# hacemos una consulta para sacar todos los valores de Parroquia
parroquia = session.query(Parroquia).all()

"""
Para abrir los archivos Instituciones-Educativas.csv
"""
openCsv = open('data/Listado-Instituciones-Educativas.csv',
               'r', encoding='utf-8')

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
    # Comparativa para ingresar los datos
    for j in parroquia:
        # Si el nombre de la parroquia coincide con la consulta guarde en cod el codigo de parroquia
        if(texto[7] == j.parroquia):
            cod = j.codigo
    # Lo guardamos el objeto Establecimiento
    ingresaEst = Establecimiento(codigo=texto[0], nombres=texto[1], nDistrito=texto[8], sostenimiento=texto[9],
                                 tipo=texto[10], modalidad=texto[11], jornada=texto[12], acceso=texto[13],
                                 numEstudiantes=int(texto[14]), numDocentes=int(texto[15]), parroquia_id=cod)

    # Guardamos en la base de datos
    session.add(ingresaEst)


# Confirmamos las transicciones
session.commit()
