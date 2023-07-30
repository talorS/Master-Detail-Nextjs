from sqlalchemy import Column, Integer, String
from config.db import Base


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False)
    content = Column(String(255), nullable=False)

    class Config:
        orm_mode = True
