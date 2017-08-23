import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.user_mock import User_Mock


def fake_user(name, email, password, birthdate):
    # Inserting mock mid-application
    return User_Mock(None, name, email, password, birthdate)


class UserTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()

    def tearDown(self):
        # mostly used for closing files and db
        pass

    @patch('biscuit.biscuit.create_user', side_effect=fake_user)
    def test_create_response(self, mock):
        response = self.app.post(
            '/user',
            data=json.dumps({
                'name': 'Goku',
                'email': 'goku@dragonball.com',
                'password': 'freeza_sux123',
                'birthdate': '30/04/1994'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
