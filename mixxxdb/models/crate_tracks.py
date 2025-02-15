from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

from .crates import Crates
from .track_locations import TrackLocations

Base = declarative_base()


class CrateTracks(Base):
    __tablename__ = "crate_tracks"
    crate_id = Column(Integer, ForeignKey(Crates.id), primary_key=True)
    track_id = Column(Integer, ForeignKey(TrackLocations.id), primary_key=True)

    __table_args__ = (UniqueConstraint("crate_id", "track_id", name="_crate_track_uc"),)
