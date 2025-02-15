from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RhythmboxLibrary(Base):
    __tablename__ = "rhythmbox_library"
    id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(String(48))
    title = Column(String(48))
    album = Column(String(48))
    year = Column(String(16))
    genre = Column(String(32))
    tracknumber = Column(String(3))
    location = Column(String(512), unique=True)
    comment = Column(String(60))
    duration = Column(Integer)
    bitrate = Column(Integer)
    bpm = Column(Float)
    key = Column(String(6))
    rating = Column(Integer)
