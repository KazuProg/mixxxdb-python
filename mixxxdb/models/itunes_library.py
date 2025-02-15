from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class iTunesLibrary(Base):
    __tablename__ = "itunes_library"
    id = Column(Integer, primary_key=True)
    artist = Column(String(48))
    title = Column(String(48))
    album = Column(String(48))
    year = Column(String(16))
    genre = Column(String(32))
    tracknumber = Column(String(3))
    location = Column(String(512))
    comment = Column(String(60))
    duration = Column(Integer)
    bitrate = Column(Integer)
    bpm = Column(Integer)
    rating = Column(Integer)
    grouping = Column(Text, default="")
    album_artist = Column(Text, default="")
