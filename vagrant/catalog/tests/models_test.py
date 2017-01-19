import unittest
from models.users import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from vagrant.catalog.models import base

class UsersTest(unittest.TestCase):

    engine = None

    def setUp(self):
        print "Setting up the UsersTest"
        engine = create_engine('sqlite:///:memory:', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        base.Base.metadata.create_all(engine)

    def test_add_user(self):
        user = User(email="foo@bar.com")
        self.session.add(user)
        self.session.commit()

        r_user = self.session.query(User).first()
        self.assertIsNotNone(r_user)
        self.assertEqual(r_user.email, "foo@bar.com", "Emails not equal")


