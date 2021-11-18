from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base



class BahanDasar(Base):

    __tablename__ = "bahanDasar"


    id = Column(Integer, primary_key=True, index=True)
    namaBahan = Column(String, index=True)
    kuantitas = Column(Integer)
