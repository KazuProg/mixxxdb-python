from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LibraryHashes(Base):
    __tablename__ = "LibraryHashes"
    directory_path = Column(String(256), primary_key=True)
    hash = Column(Integer)
    directory_deleted = Column(Integer)
    needs_verification = Column(Integer, default=0)
