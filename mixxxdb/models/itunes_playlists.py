from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class iTunesPlaylists(Base):
    __tablename__ = "itunes_playlists"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
