from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # se importa el operador and

# se importa las clases de archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta que devuelve  los establecimientos de la provincia de Loja.
print("--- Establecimientos de la provincia de Loja ---")

"""
En la consulta sacamos el establecimiento en el filtramos en provincia el nombre de la provincia sea igual a Loja
"""
consulta_1_1 = session.query(Establecimiento).join(
    Parroquia, Canton, Provincia).filter(Provincia.provincia == 'LOJA').all()

# Variable que saca el número de registros de consulta_1_1
numEstloja = len(consulta_1_1)
# impresión de los resultados de consulta_1_1
for i in consulta_1_1:
    print(i)

print("número total de establecimientos \
    en la provincia de loja : %d \n\n\n" % (numEstloja))

# Todos los establecimientos del cantón de Loja.
print("--- Establecimientos del cantón de Loja ---")
"""
En la consulta sacamos el establecimiento en el filtramos en canton el nombre de la canton sea igual a Loja
"""
consulta_1_2 = session.query(Establecimiento).join(
    Parroquia, Canton, Provincia).filter(Canton.canton == 'LOJA').all()
# Variable que saca el número de registros de consulta_1_2
numEst_cantonloja = len(consulta_1_2)
# impresión de los resultados de consulta_1_2
for i in consulta_1_2:
    print(i)


print("Número total de establecimientos en el cantón de Loja \
    : %d \n\n\n" % (numEst_cantonloja))
