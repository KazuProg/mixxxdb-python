"""
Library model representing the main music library table in Mixxx database.
"""
from typing import Optional
from datetime import datetime

from sqlalchemy import (
    func,
    Column,
    Integer,
    String,
    Float,
    BLOB,
    TEXT,
    DateTime,
    REAL,
    ForeignKey,
)

from . import Base
from .track_locations import TrackLocations


class Library(Base):
    __tablename__ = "library"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(String(64))
    title = Column(String(64))
    album = Column(String(64))
    year = Column(String(16))
    genre = Column(String(64))
    tracknumber = Column(String(3))
    location = Column(Integer, ForeignKey(TrackLocations.id))
    comment = Column(String(256))
    url = Column(String(256))
    duration = Column(Float)
    bitrate = Column(Integer)
    samplerate = Column(Integer)
    cuepoint = Column(Integer)
    bpm = Column(Float)
    wavesummaryhex = Column(BLOB)
    channels = Column(Integer)
    datetime_added = Column(DateTime, server_default=func.now())
    mixxx_deleted = Column(Integer)
    played = Column(Integer)
    header_parsed = Column(Integer, default=0)
    filetype = Column(String(8), default="?")
    replaygain = Column(Float, default=0.0)
    timesplayed = Column(Integer, default=0)
    rating = Column(Integer, default=0)
    key = Column(String(8), default="")
    beats = Column(BLOB)
    beats_version = Column(TEXT)
    composer = Column(String(64), default="")
    bpm_lock = Column(Integer, default=0)
    beats_sub_version = Column(TEXT, default="")
    keys = Column(BLOB)
    keys_version = Column(TEXT)
    keys_sub_version = Column(TEXT)
    key_id = Column(Integer, default=0)
    grouping = Column(TEXT, default="")
    album_artist = Column(TEXT, default="")
    coverart_source = Column(Integer, default=0)
    coverart_type = Column(Integer, default=0)
    coverart_location = Column(TEXT, default="")
    coverart_hash = Column(Integer, default=0)
    replaygain_peak = Column(REAL, default=-1.0)
    tracktotal = Column(TEXT, default="//")
    color = Column(Integer)
    coverart_color = Column(Integer)
    coverart_digest = Column(BLOB)
    last_played_at = Column(DateTime, default=None)
    source_synchronized_ms = Column(Integer, default=None)
