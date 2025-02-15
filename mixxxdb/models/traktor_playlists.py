from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TraktorPlaylists(Base):
    __tablename__ = "traktor_playlists"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
