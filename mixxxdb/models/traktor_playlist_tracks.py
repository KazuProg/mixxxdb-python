from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .traktor_playlists import TraktorPlaylists
from .traktor_library import TraktorLibrary

Base = declarative_base()


class TraktorPlaylistTracks(Base):
    __tablename__ = "traktor_playlist_tracks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    playlist_id = Column(Integer, ForeignKey(TraktorPlaylists.id))
    track_id = Column(Integer, ForeignKey(TraktorLibrary.id))
    position = Column(Integer, default=0)
