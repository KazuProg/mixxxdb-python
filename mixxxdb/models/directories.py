from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Directories(Base):
    __tablename__ = "directories"
    directory = Column(Text, primary_key=True, unique=True)
