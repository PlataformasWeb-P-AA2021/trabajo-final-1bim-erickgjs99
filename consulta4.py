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

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
print("--- Establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. ---\n\n\n")
""""
Consultamos en la clase Establecimiento filtramos el número de docentes sea mayor a 100 y sea ordenado por el
número de estudiantes
"""
consulta_3_1 = session.query(Establecimiento).filter(
    Establecimiento.numDocentes > 100).order_by(Establecimiento.numEstudiantes).all()


# impresión de los resultados de consulta_3_1
for i in consulta_3_1:
    print(i)
# salto de linea
print("\n\n\n")

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
print("--- Establecimientos ordenados por número de profesores; que tengan más de 100 profesores. ---\n\n\n")
""""
Consultamos en la clase Establecimiento, filtramos el numero de docentes sea mayor a 100 y ordenamos por el numero de docentes
"""
consulta_3_2 = session.query(Establecimiento).filter(
    Establecimiento.numDocentes > 100).order_by(Establecimiento.numDocentes).all()


# impresión de los resultados de consulta_3_2
for i in consulta_3_2:
    print(i)
