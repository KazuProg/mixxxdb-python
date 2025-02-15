from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .rhythmbox_playlists import RhythmboxPlaylists
from .rhythmbox_library import RhythmboxLibrary

Base = declarative_base()


class RhythmboxPlaylistTracks(Base):
    __tablename__ = "rhythmbox_playlist_tracks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    playlist_id = Column(Integer, ForeignKey(RhythmboxPlaylists.id))
    track_id = Column(Integer, ForeignKey(RhythmboxLibrary.id))
    position = Column(Integer, default=0)
