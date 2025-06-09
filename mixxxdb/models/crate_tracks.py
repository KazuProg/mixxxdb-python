from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint

from . import Base
from .crates import Crates
from .library import Library


class CrateTracks(Base):
    __tablename__ = "crate_tracks"
    
    crate_id = Column(Integer, ForeignKey(Crates.id), primary_key=True, nullable=False)
    track_id = Column(Integer, ForeignKey(Library.id), primary_key=True, nullable=False)

    __table_args__ = (
        UniqueConstraint("crate_id", "track_id", name="_crate_track_uc"),
    )
