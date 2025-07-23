from sqlalchemy import Column, String, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TH_tbl(Base):
    __tablename__ = 'TH_tbl'
    id = Column(String(8), primary_key=True)
    dt = Column(TIMESTAMP, primary_key=True)
    temp = Column(Float, nullable=False)
    humid = Column(Float, nullable=False)