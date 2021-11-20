from sqlalchemy import Column, Integer, String

from database import Base



class BahanDasar(Base):

    __tablename__ = "bahanDasar"


    id = Column(Integer, primary_key=True)
    namaBahan = Column(String)
    kuantitas = Column(Integer)
