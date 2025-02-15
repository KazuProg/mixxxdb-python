import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import *
from .utils import get_mixxx_db_path


class MixxxDB:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = get_mixxx_db_path()

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database file not found: {db_path}")

        try:
            self.engine = create_engine(f"sqlite:///{db_path}")
        except Exception as e:
            raise

        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
