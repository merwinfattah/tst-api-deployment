from pydantic import BaseModel

class BahanDasar(BaseModel):
    id: int
    nama: str
    kuantitas: int

class BahanDasarUpdate(BaseModel):
    id: int
    nama: str
    kuantitas: int