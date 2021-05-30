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

# Los cantones que tiene establecimientos con 0 número de profesores
print("--- Cantones que tiene establecimientos con 0 número de profesores ---")
"""
Consultamos en la clase Establecimiento y filtramos en Establecimiento el numero de docentes sea igual a 0
"""
consulta_3_1 = session.query(Establecimiento).filter(
    Establecimiento.numDocentes == 0).all()
# Variable que saca el número de registros de consulta_3_1
numDoc = len(consulta_3_1)
# impresión de los resultados de consulta_3_1
for i in consulta_3_1:
    print(i)

print("\n\nnúmero de cantones que tienen establecimientos 0 docentes %s\n\n\n\n" % (numDoc))

# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
print("--- Establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21 ---\n\n\n")
""""
Consultamos en la clase Establecimiento unimos parroquia y filtramos que el numero de estudiantes 
sea mayor igual a 21 y que su parroquia sea catacocha
"""
consulta_3_2 = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.numEstudiantes >= 21,
                                                                          Parroquia.parroquia == "CATACOCHA")).all()
# Variable que saca el número de registros de consulta_3_2
numParr = len(consulta_3_2)

# impresión de los resultados de consulconsulta_3_2ta_3_1
for i in consulta_3_2:
    print(i)

print("\n\nNúmero establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21 %s\n\n\n\n" % (numParr))
