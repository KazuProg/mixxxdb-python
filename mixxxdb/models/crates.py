from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Crates(Base):
    __tablename__ = "crates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(48), unique=True, nullable=False)
    count = Column(Integer, default=0)
    show = Column(Boolean, default=True)
    locked = Column(Boolean, default=False)
    autodj_source = Column(Integer, default=0)
