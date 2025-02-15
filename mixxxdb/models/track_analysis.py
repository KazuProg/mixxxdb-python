from sqlalchemy import func, Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .track_locations import TrackLocations

Base = declarative_base()


class TrackAnalysis(Base):
    __tablename__ = "track_analysis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey(TrackLocations.id))
    type = Column(String(512))
    description = Column(String(1024))
    version = Column(String(512))
    created = Column(DateTime, default=func.now())
    data_checksum = Column(String(512))
