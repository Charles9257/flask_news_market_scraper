import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from app import create_app
from app.db.db_utils import db
from app.db.models import Article
from app.config import TestConfig

class MainRoutesTestCase(unittest.TestCase):
    def setUp(self):
        # Pass config class directly if your factory expects it
        self.app = create_app(config_class=TestConfig)  
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        db.create_all()

        article = Article(title="Test Article", link="http://example.com")
        db.session.add(article)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Charles Ugwute Ogbonna', response.data)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

if __name__ == '__main__':
    unittest.main()
