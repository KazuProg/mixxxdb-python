from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Settings(Base):
    __tablename__ = "settings"
    name = Column(Text, primary_key=True, unique=True, nullable=False)
    value = Column(Text)
    locked = Column(Integer, default=0)
    hidden = Column(Integer, default=0)
