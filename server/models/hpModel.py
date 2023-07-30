from sqlalchemy import Column, Integer, String
from config.db import Base


class HpModel(Base):
    __tablename__ = 'hpData'

    id = Column(Integer, primary_key=True, autoincrement=True)
    headline = Column(String(255), nullable=False)

    class Config:
        orm_mode = True
