from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
import databases
import crud, models, schemas
from database import SessionLocal, engine, SQLALCHEMY_DATABASE_URL

models.Base.metadata.create_all(bind=engine)
database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/bahanDasar")
async def add_bahan_dasar(bahanDasar: schemas.BahanDasar, db: Session = Depends(get_db)):
    db_item = crud.add_item(db, bahanDasar)
    return db_item

@app.put("/bahanDasar")
async def upadate_bahan_dasar(id_bahan: int, nama_bahan: str, kuantitas: int, db: Session = Depends(get_db)):
    db_bahan = crud.update_item(db, id_bahan, nama_bahan, kuantitas)
    if db_bahan is None:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return db_bahan

@app.get("/bahanDasar")
async def visualisasi_bahan_dasar(db : Session = Depends(get_db)):
     return db.query(models.BahanDasar).all()