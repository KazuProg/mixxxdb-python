from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .itunes_playlists import iTunesPlaylists
from .itunes_library import iTunesLibrary

Base = declarative_base()


class iTunesPlaylistTracks(Base):
    __tablename__ = "itunes_playlist_tracks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    playlist_id = Column(Integer, ForeignKey(iTunesPlaylists.id))
    track_id = Column(Integer, ForeignKey(iTunesLibrary.id))
    position = Column(Integer, default=0)
