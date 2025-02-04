from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class Aspirante(Base):
    __tablename__ = "aspirantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    carrera_deseada = Column(String)
    admitido = Column(Boolean, default=False)
    carrera_asignada = Column(String, nullable=True)