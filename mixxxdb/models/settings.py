from sqlalchemy import Column, Text, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Settings(Base):
    __tablename__ = "settings"
    name = Column(Text, primary_key=True, unique=True)
    value = Column(Text)
    locked = Column(Boolean, default=False)
    hidden = Column(Boolean, default=False)
