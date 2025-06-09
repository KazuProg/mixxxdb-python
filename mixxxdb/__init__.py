"""
Mixxx Database Python Library

A Python library for reading and analyzing Mixxx DJ software databases.
Provides SQLAlchemy ORM models for all Mixxx database tables and utilities
for database access and analysis.

Example:
    >>> from mixxxdb import MixxxDB, Library
    >>> db = MixxxDB()
    >>> tracks = db.get_all_tracks()
    >>> print(f"Found {len(tracks)} tracks")
"""

from .mixxxdb import MixxxDB
from .models import *
from .utils import get_mixxx_db_path, get_mixxx_settings_dir, verify_mixxx_db_exists

__version__ = "1.39.0"
__author__ = "KazuProg"

__all__ = [
    # Main database class
    "MixxxDB",
    
    # Utility functions
    "get_mixxx_db_path",
    "get_mixxx_settings_dir", 
    "verify_mixxx_db_exists",
    
    # Base class
    "Base",
    
    # Core models
    "Library",
    "TrackLocations",
    "Crates",
    "CrateTracks",
    "Playlists",
    "PlaylistTracks",
    "Cues",
    "Settings",
    "Directories",
    "LibraryHashes",
    "TrackAnalysis",
    
    # External library models
    "iTunesLibrary",
    "iTunesPlaylistTracks", 
    "iTunesPlaylists",
    "RhythmboxLibrary",
    "RhythmboxPlaylistTracks",
    "RhythmboxPlaylists",
    "TraktorLibrary",
    "TraktorPlaylistTracks",
    "TraktorPlaylists",
]
