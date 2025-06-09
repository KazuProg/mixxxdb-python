from sqlalchemy import Column, Integer, ForeignKey, DateTime

from . import Base
from .playlists import Playlists
from .library import Library


class PlaylistTracks(Base):
    __tablename__ = "PlaylistTracks"
    
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey(Playlists.id))
    track_id = Column(Integer, ForeignKey(Library.id))
    position = Column(Integer)
    pl_datetime_added = Column(DateTime)
