from pydantic import BaseModel

class BahanDasar(BaseModel):
    id: int
    namaBahan: str
    kuantitas: int

class BahanDasarUpdate(BaseModel):
    id: int
    namaBahan: str
    kuantitas: int