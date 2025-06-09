"""
Mixxx database connection and management.
"""
import os
from pathlib import Path
from typing import Optional, List
from contextlib import contextmanager

from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from .models import Library, Crates, Playlists
from .utils import get_mixxx_db_path


class MixxxDB:
    """
    Mixxx database connection and management class.
    
    Provides a high-level interface for connecting to and querying
    the Mixxx SQLite database.
    """
    
    def __init__(self, db_path: Optional[str] = None) -> None:
        """
        Initialize database connection.
        
        Args:
            db_path: Path to Mixxx database file. If None, uses default location.
            
        Raises:
            FileNotFoundError: If database file doesn't exist.
            SQLAlchemyError: If database connection fails.
        """
        if db_path is None:
            db_path = get_mixxx_db_path()
            
        self.db_path = Path(db_path)
        
        if not self.db_path.exists():
            raise FileNotFoundError(f"Database file not found: {self.db_path}")
            
        try:
            # Create engine with better error handling
            self.engine: Engine = create_engine(
                f"sqlite:///{self.db_path}",
                echo=False,
                pool_pre_ping=True,
                connect_args={"check_same_thread": False}
            )
            
            # Test connection
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                
        except Exception as e:
            raise SQLAlchemyError(f"Failed to connect to database: {e}") from e
            
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        """
        Get a new database session.
        
        Returns:
            SQLAlchemy session instance.
        """
        return self.Session()
    
    @contextmanager
    def session_scope(self):
        """
        Context manager for database sessions with automatic cleanup.
        
        Usage:
            with db.session_scope() as session:
                tracks = session.query(Library).all()
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_all_tracks(self) -> List[Library]:
        """Get all tracks from the library."""
        with self.session_scope() as session:
            return session.query(Library).all()
    
    def get_track_by_id(self, track_id: int) -> Optional[Library]:
        """Get a specific track by ID."""
        with self.session_scope() as session:
            return session.query(Library).filter(Library.id == track_id).first()
    
    def get_tracks_by_artist(self, artist: str) -> List[Library]:
        """Get all tracks by a specific artist."""
        with self.session_scope() as session:
            return session.query(Library).filter(Library.artist.ilike(f"%{artist}%")).all()
    
    def get_all_crates(self) -> List[Crates]:
        """Get all crates."""
        with self.session_scope() as session:
            return session.query(Crates).all()
    
    def get_crate_by_name(self, name: str) -> Optional[Crates]:
        """Get a crate by name."""
        with self.session_scope() as session:
            return session.query(Crates).filter(Crates.name == name).first()
    
    def get_all_playlists(self) -> List[Playlists]:
        """Get all playlists.""" 
        with self.session_scope() as session:
            return session.query(Playlists).all()
    
    def get_playlist_by_name(self, name: str) -> Optional[Playlists]:
        """Get a playlist by name."""
        with self.session_scope() as session:
            return session.query(Playlists).filter(Playlists.name == name).first()
    
    @property
    def db_info(self) -> dict:
        """Get database information."""
        with self.session_scope() as session:
            track_count = session.query(Library).count()
            crate_count = session.query(Crates).count() 
            playlist_count = session.query(Playlists).count()
            
            return {
                "path": str(self.db_path),
                "tracks": track_count,
                "crates": crate_count,
                "playlists": playlist_count,
            }
    
    def close(self) -> None:
        """Close database connection."""
        if hasattr(self, 'engine'):
            self.engine.dispose()
