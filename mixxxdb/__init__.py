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
    # Main classes and utilities
    "Base",
    "MixxxDB",
    "get_mixxx_db_path",
    "get_mixxx_settings_dir",
    "verify_mixxx_db_exists",
    
    # Database models
    "Crates",
    "CrateTracks",
    "Cues",
    "Directories",
    "iTunesLibrary",
    "iTunesPlaylistTracks",
    "iTunesPlaylists",
    "Library",
    "LibraryHashes",
    "Playlists",
    "PlaylistTracks",
    "RhythmboxLibrary",
    "RhythmboxPlaylistTracks",
    "RhythmboxPlaylists",
    "Settings",
    "TrackAnalysis",
    "TrackLocations",
    "TraktorLibrary",
    "TraktorPlaylistTracks",
    "TraktorPlaylists",
]
