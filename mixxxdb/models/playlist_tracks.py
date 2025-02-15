from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .playlists import Playlists
from .track_locations import TrackLocations

Base = declarative_base()


class PlaylistTracks(Base):
    __tablename__ = "PlaylistTracks"
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey(Playlists.id))
    track_id = Column(Integer, ForeignKey(TrackLocations.id))
    position = Column(Integer)
    pl_datetime_added = Column(DateTime)
