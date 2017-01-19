from sqlalchemy import create_engine

from models.base import Base
from config import DB_FILENAME

engine = create_engine('sqlite:///%s' % DB_FILENAME, echo=True)

# Create the tables
Base.metadata.create_all(engine)

