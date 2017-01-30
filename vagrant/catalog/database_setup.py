from catalog.models.base import Base
import catalog.models.categories
import catalog.models.items
import catalog.models.users
from catalog import engine

# Create the tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

