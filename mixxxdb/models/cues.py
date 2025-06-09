from sqlalchemy import Column, Integer, ForeignKey, Text

from . import Base
from .library import Library


class Cues(Base):
    __tablename__ = "cues"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey(Library.id), nullable=False)
    type = Column(Integer, default=0, nullable=False)
    position = Column(Integer, default=-1, nullable=False)
    length = Column(Integer, default=0, nullable=False)
    hotcue = Column(Integer, default=-1, nullable=False)
    label = Column(Text, default="", nullable=False)
    color = Column(Integer, default=4294901760, nullable=False)
