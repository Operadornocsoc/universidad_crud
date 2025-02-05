# app/schemas/aspirante.py
from pydantic import BaseModel

class AspiranteBase(BaseModel):
    nombre: str
    carrera_deseada: str

class AspiranteCreate(AspiranteBase):
    pass

class Aspirante(AspiranteBase):
    id: int
    admitido: bool
    carrera_asignada: str | None = None

    class Config:
        orm_mode = True