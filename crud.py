from sqlalchemy.orm import Session
from sqlalchemy import update
import models, schemas



def add_item(db: Session, bahanDasar: schemas.BahanDasar):
    new_item = models.BahanDasar(
    id=bahanDasar.id, 
    nama=bahanDasar.nama, 
    kuantitas=bahanDasar.kuantitas
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, id_bahan: int, nama: str, kuantitas: int):
    db_bahan_to_update = db.query(models.BahanDasar).filter(models.BahanDasar.id == id_bahan).first()
    db_bahan_to_update.kuantitas = kuantitas
    db_bahan_to_update.nama = nama
    db.add(db_bahan_to_update)
    db.commit()
    db.refresh(db_bahan_to_update)
    return db_bahan_to_update
   
    
    