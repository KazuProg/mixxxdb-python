from sqlalchemy import Column, Text, Integer

from . import Base


class Settings(Base):
    __tablename__ = "settings"
    
    name = Column(Text, primary_key=True, unique=True, nullable=False)
    value = Column(Text)
    locked = Column(Integer, default=0)
    hidden = Column(Integer, default=0)
