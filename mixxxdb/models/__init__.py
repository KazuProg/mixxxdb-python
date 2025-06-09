from sqlalchemy.ext.declarative import declarative_base

# 共通のベースクラス
Base = declarative_base()

# Models
from .library_hashes import LibraryHashes
from .playlist_tracks import PlaylistTracks
from .playlists import Playlists
from .crate_tracks import CrateTracks
from .crates import Crates
from .cues import Cues
from .directories import Directories
from .itunes_library import iTunesLibrary
from .itunes_playlist_tracks import iTunesPlaylistTracks
from .itunes_playlists import iTunesPlaylists
from .library import Library
from .rhythmbox_library import RhythmboxLibrary
from .rhythmbox_playlist_tracks import RhythmboxPlaylistTracks
from .rhythmbox_playlists import RhythmboxPlaylists
from .settings import Settings
from .track_analysis import TrackAnalysis
from .track_locations import TrackLocations
from .traktor_library import TraktorLibrary
from .traktor_playlist_tracks import TraktorPlaylistTracks
from .traktor_playlists import TraktorPlaylists

__all__ = [
    "Base",
    "LibraryHashes",
    "PlaylistTracks",
    "Playlists",
    "CrateTracks",
    "Crates",
    "Cues",
    "Directories",
    "iTunesLibrary",
    "iTunesPlaylistTracks",
    "iTunesPlaylists",
    "Library",
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
