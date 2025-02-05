# app/routers/aspirantes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/aspirantes/", response_model=schemas.Aspirante)
def create_aspirante(aspirante: schemas.AspiranteCreate, db: Session = Depends(get_db)):
    db_aspirante = models.Aspirante(**aspirante.dict())
    db.add(db_aspirante)
    db.commit()
    db.refresh(db_aspirante)
    return db_aspirante

@router.get("/aspirantes/", response_model=list[schemas.Aspirante])
def read_aspirantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aspirantes = db.query(models.Aspirante).offset(skip).limit(limit).all()
    return aspirantes

@router.get("/aspirantes/{aspirante_id}", response_model=schemas.Aspirante)
def read_aspirante(aspirante_id: int, db: Session = Depends(get_db)):
    aspirante = db.query(models.Aspirante).filter(models.Aspirante.id == aspirante_id).first()
    if aspirante is None:
        raise HTTPException(status_code=404, detail="Aspirante no encontrado")
    return aspirante

@router.put("/aspirantes/{aspirante_id}", response_model=schemas.Aspirante)
def update_aspirante(aspirante_id: int, aspirante: schemas.AspiranteCreate, db: Session = Depends(get_db)):
    db_aspirante = db.query(models.Aspirante).filter(models.Aspirante.id == aspirante_id).first()
    if db_aspirante is None:
        raise HTTPException(status_code=404, detail="Aspirante no encontrado")
    for key, value in aspirante.dict().items():
        setattr(db_aspirante, key, value)
    db.commit()
    db.refresh(db_aspirante)
    return db_aspirante

@router.delete("/aspirantes/{aspirante_id}", response_model=schemas.Aspirante)
def delete_aspirante(aspirante_id: int, db: Session = Depends(get_db)):
    aspirante = db.query(models.Aspirante).filter(models.Aspirante.id == aspirante_id).first()
    if aspirante is None:
        raise HTTPException(status_code=404, detail="Aspirante no encontrado")
    db.delete(aspirante)
    db.commit()
    return aspirante