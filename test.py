import unittest
from app import app, db, User

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()
            user = User(username="testuser", password="testpassword")
            db.session.add(user)
            db.session.commit()

    def login(self):
        return self.app.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)

    def test_home(self):
        self.login()
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        with app.app_context():
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
