from sqlalchemy import Column, Integer, String, DateTime

from . import Base


class Playlists(Base):
    __tablename__ = "Playlists"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(48))
    position = Column(Integer)
    hidden = Column(Integer, default=0, nullable=False)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    locked = Column(Integer, default=0)
