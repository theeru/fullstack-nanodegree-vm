from sqlalchemy.ext.declarative import declarative_base
from .. import session


Base = declarative_base()
Base.query = session.query_property()