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
