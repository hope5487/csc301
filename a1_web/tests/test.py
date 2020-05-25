import unittest
from main import app
from flask import Flask, session


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        app.config['SECRET_KEY'] = '123'

    def test_login(self):
        self.app = app.test_client()
        with app.test_client() as client:
            client.post('/login', data=dict(username='s', password='s'))
            with client.session_transaction() as sess:
                assert sess['logged_in']
        return ''

    def test_logout(self):
        self.app = app.test_client()
        with app.test_client() as client:
            client.post('/login', data=dict(username='s', password='s'))
            with client.session_transaction() as sess:
                assert sess['logged_in']
        return ''


if __name__ == '__main__':
    unittest.main()
