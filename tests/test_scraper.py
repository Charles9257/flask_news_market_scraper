# tests/test_scraper.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from app.scraper.news_scraper import fetch_articles

MOCK_HTML = '''
<html>
    <body>
        <div class="article">
            <h2>Sample Article</h2>
            <a href="/sample-article">Read more</a>
        </div>
    </body>
</html>
'''

class FetchArticlesTest(unittest.TestCase):
    @patch('app.scraper.news_scraper.requests.get')
    def test_fetch_articles(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = MOCK_HTML

        url = "http://example.com"
        articles = fetch_articles(url)

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], 'Sample Article')
        self.assertEqual(articles[0]['link'], '/sample-article')

if __name__ == '__main__':
    unittest.main()
