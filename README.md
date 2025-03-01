# mixxxdb-python

This repository provides the `mixxxdb` Python library, which provides an interface to the Mixxx database using SQLAlchemy. This library is used as `MixxxDB`.

## Features

- Represents the Mixxx database structure as Python classes.
- Enables flexible database operations using SQLAlchemy.
- Simplifies database access and initialization with the `MixxxDB` class.

## Usage

```python
from mixxxdb import MixxxDB, Library  # Import the models

# Connect to the database (using the default path)
db = MixxxDB()

# Or, connect with a specified path:
# db = MixxxDB("path/to/mixxxdb.sqlite")

session = db.get_session()

# Perform database operations
tracks = session.query(Library).all()
for track in tracks:
    print(track.title)

session.close()
```

## MixxxDB Class

The `MixxxDB` class simplifies accessing and initializing the Mixxx database.

### Constructor

```python
MixxxDB(db_path=None)
```

- `db_path`: The path to the database file (optional). If not specified, the default path (see [Mixxx Settings Directory](https://manual.mixxx.org/2.5/en/chapters/appendix/settings_directory#location) for details) is used.

### Methods

- `get_session()`: Retrieves a SQLAlchemy session object.

## Models

Model classes corresponding to each table are provided:

- `LibraryHashes`
- `PlaylistTracks`
- `Playlists`
- `CrateTracks`
- `Crates`
- `Cues`
- `Directories`
- `iTunesLibrary`
- `iTunesPlaylistTracks`
- `iTunesPlaylists`
- `Library`
- `RhythmboxLibrary`
- `RhythmboxPlaylistTracks`
- `RhythmboxPlaylists`
- `Settings`
- `TrackAnalysis`
- `TrackLocations`
- `TraktorLibrary`
- `TraktorPlaylistTracks`
- `TraktorPlaylists`

## Example

### Get all tracks

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

tracks = session.query(Library).all()
for track in tracks:
    print(track.title)

session.close()
```

### Search for tracks by artist

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

tracks = session.query(Library).filter(Library.artist == "Artist Name").all()

for track in tracks:
    print(track.title)

session.close()
```

### Search for tracks with "test" in the title

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

tracks = session.query(Library).filter(Library.title.like("%test%")).all()
for track in tracks:
    print(track.title)

session.close()
```

### Search for tracks by playlist name

```python
from mixxxdb import MixxxDB, Playlists, PlaylistTracks, TrackLocations, Library

db = MixxxDB()
session = db.get_session()

playlist_name = "MyPlaylist"

tracks = (
    session.query(PlaylistTracks.position, Library.title)
    .select_from(Playlists)
    .join(PlaylistTracks)
    .join(TrackLocations)
    .join(Library)
    .filter(Playlists.name == playlist_name)
    .order_by(PlaylistTracks.position)
    .all()
)

for track in tracks:
    print(f"{track[0]}: {track[1]}")

session.close()
```

### Add a new track

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

# This is a simplified example of how to add a record to the database.
# In reality, you'll likely need to add other initial values and records.
new_track = Library(title="New Track Title", artist="New Artist", album="New Album")
session.add(new_track)
session.commit()

print(f"Added track with ID: {new_track.id}")

session.close()
```

### Update a track

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

track_to_update = session.query(Library).filter(Library.title == "New Track Title").first()

if track_to_update:
  track_to_update.album = "Updated Album Name"
  session.commit()
  print(f"Updated track with ID: {track_to_update.id}")
else:
  print("Track not found.")

session.close()
```

### Delete a track

```python
from mixxxdb import MixxxDB, Library

db = MixxxDB()
session = db.get_session()

# This is a simplified example of how to delete a record to the database.
# In reality, you'll likely need to delete other initial values and records.
track_to_delete = session.query(Library).filter(Library.title == "New Track Title").first()

if track_to_delete:
  session.delete(track_to_delete)
  session.commit()
  print(f"Deleted track with ID: {track_to_delete.id}")
else:
  print("Track not found.")

session.close()
```
