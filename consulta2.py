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

# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
print("--- Establecimientos únicamente en la jornada Nocturna ---\n\n\n")
"""
Consulta en la cual sacamos Parroquia y aplicamos un filter en el cual comparamos que jornada sea igual a "Nocturna" 
"""
consulta_2_1 = session.query(Parroquia).join(Establecimiento).filter(
    Establecimiento.jornada == 'Nocturna').all()
# Variable que saca el número de registros de consulta_2_1
numNocturna = len(consulta_2_1)
# impresión de los resultados de consulta_2_1
for i in consulta_2_1:
    print(i)

print("\n\n\nNúmero de establecimientos únicamente en la jornada Nocturna: %d\n\n\n" % (numNocturna))


# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
print("--- Establecimientos con número de estudiantes tales como: 448, 450, 451, 454, 458, 459 ---\n")
"""
Consulta que sacamos el canton en el cual unimos parroquia y establecimiento, y filtamos todos los numeros 
de estudiantes requeridos en el enunciado 
"""
consulta_2_2 = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.numEstudiantes == 448, Establecimiento.numEstudiantes == 450,
                                                                                 Establecimiento.numEstudiantes == 451, Establecimiento.numEstudiantes == 454, Establecimiento.numEstudiantes == 458, Establecimiento.numEstudiantes == 459)).all()

# impresión de los resultados de consulta_2_2
for i in consulta_2_2:
    print(i)
