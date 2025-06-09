from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .playlists import Playlists
from .library import Library

Base = declarative_base()


class PlaylistTracks(Base):
    __tablename__ = "PlaylistTracks"
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey(Playlists.id))
    track_id = Column(Integer, ForeignKey(Library.id))
    position = Column(Integer)
    pl_datetime_added = Column(DateTime)
