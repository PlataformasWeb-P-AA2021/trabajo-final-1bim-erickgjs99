# Importación sqlalchmy para trabajar
from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creamos la Clase establecimiento


class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=False)
    nombres = Column(String, nullable=false)
    nDistrito = Column(String, nullable=false)
    sostenimiento = Column(String, nullable=false)
    tipo = Column(String, nullable=false)
    modalidad = Column(String, nullable=false)
    jornada = Column(String, nullable=false)
    acceso = Column(String, nullable=false)
    numEstudiantes = Column(Integer, nullable=false)
    numDocentes = Column(Integer, nullable=false)
    parroquia_id = Column(String, ForeignKey('parroquia.codigo'))
    parroquia = relationship("Parroquia", back_populates="establecimiento")
    """ Función repr genera representaciones que pueden ser leídas por el intérprete, en las cuales le mandamos
    una cadena de toda la información de Establecimientos"""

    def __repr__(self):
        return "Establecimiento: nombre=%s - Numero de distrito=%s - Sostenimiento=%s - Tipo=%s - Modalidad=%s - \
        Jornada=%s - Acceso=%s - Num. Estudiantes=%d - Num. Docenctes=%d - parroquia_id=%s" % (
            self.nombres,
            self.nDistrito,
            self.sostenimiento,
            self.tipo,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.numEstudiantes,
            self.numDocentes,
            self.parroquia_id)

# Creamos la Clase Provincia


class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=false)
    provincia = Column(String, nullable=False)
    cantones = relationship("Canton", back_populates="provincia")
    """ Función repr genera representaciones que pueden ser leídas por el intérprete, en las cuales le mandamos
    una cadena de toda la información de Provincia"""

    def __repr__(self):
        return "Provincia: codigo=%s - nombre=%s" % (
            self.codigo,
            self.provincia
        )

# Creamos la Clase Canton


class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=false)
    canton = Column(String, nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    provincia_id = Column(String, ForeignKey('provincia.codigo'))
    provincia = relationship("Provincia", back_populates="cantones")

    """ Función repr genera representaciones que pueden ser leídas por el intérprete, en las cuales le mandamos
    una cadena de toda la información de class Canton:
    """

    def __repr__(self):
        return "Canton: codigo=%s - nombre=%s" % (
            self.codigo,
            self.canton
        )

# Creamos la Clase Parroquia


class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=false)
    parroquia = Column(String, nullable=False)
    establecimiento = relationship(
        "Establecimiento", back_populates="parroquia")
    canton_id = Column(String, ForeignKey('canton.codigo'))
    canton = relationship("Canton", back_populates="parroquias")

    """ Función repr genera representaciones que pueden ser leídas por el intérprete, en las cuales le mandamos
    una cadena de toda la información de class Parroquia:
    """

    def __repr__(self):
        return "Parroquia: codigo=%s - nombre=%s" % (
            self.codigo,
            self.parroquia
        )


# Crea toda las tablas establecidas anteriormente
Base.metadata.create_all(engine)
