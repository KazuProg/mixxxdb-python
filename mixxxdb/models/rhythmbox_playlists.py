from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RhythmboxPlaylists(Base):
    __tablename__ = "rhythmbox_playlists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
