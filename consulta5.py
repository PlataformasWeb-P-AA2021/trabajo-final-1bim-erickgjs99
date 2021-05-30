from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and

# se importa las clases de archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
print("--- Establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena Permanente en tipo de educación. ---\n\n\n")

"""
Consultamos los establecimientos lo unimos con parroquia y lo filtramos por el número de docentes sea mayor a 20
y que el tipo sea "Permanente". por ultimo lo ordenamos por parroquia
"""
consulta_5_1 = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.numDocentes > 20,
                                                                          Establecimiento.tipo.like("%Permanente%"))).order_by(Parroquia.parroquia).all()
# impresión de los resultados de consulta_5_1
for i in consulta_5_1:
    print(i)

# Variable que saca el número de registros de consulta_5_1
numParr = len(consulta_5_1)
print("\n\n Número de establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena Permanente en tipo de educación.: %d\n\n" % (numParr))


# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02
print("--- Establecimientos ordenados por sostenimiento y tengan código de distrito 11D02 ---\n\n")
""""
Consultamos los establecimientos y lo unimos con parroquia y filtramos por el número de distrito sea igual
a "11D02" y ordenamo por el sostenimiento
"""
consulta_5_2 = session.query(Establecimiento).join(Parroquia).filter(
    Establecimiento.nDistrito == '11D02').order_by(Establecimiento.sostenimiento).all()

# impresión de los resultados de consulta_5_2
for i in consulta_5_2:
    print(i)

# Variable que saca el número de registros de consulta_5_2
numDist = len(consulta_5_2)


print("\n\n Número de establecimientos ordenados por sostenimiento y tengan código de distrito 11D02: %d" % (numDist))
