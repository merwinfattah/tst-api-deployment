from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base



class BahanDasar(Base):

    __tablename__ = "bahanDasar"


    id = Column(Integer, primary_key=True)
    namaBahan = Column(String)
    kuantitas = Column(Integer)
