from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DB_FILENAME = 'catalog.db'

engine = create_engine('sqlite:///%s' % DB_FILENAME, echo=True)

session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush=False))

