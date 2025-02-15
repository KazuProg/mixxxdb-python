from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

from .track_locations import TrackLocations

Base = declarative_base()


class Cues(Base):
    __tablename__ = "cues"
    id = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey(TrackLocations.id))
    type = Column(Integer, default=0)
    position = Column(Integer, default=-1)
    length = Column(Integer, default=0)
    hotcue = Column(Integer, default=-1)
    label = Column(Text, default="")
    color = Column(Integer, default=4294901760)
