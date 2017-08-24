import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.user_mock import User_Mock


def fake_user(name, email, password, birthdate):
    # Inserting mock mid-application
    return User_Mock(None, name, email, password, birthdate)


class UserTestCase(unittest.TestCase):

    @patch('biscuit.biscuit.create_user', side_effect=fake_user)
    def setUp(self, mock):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.response = self.app.post(
            '/user',
            data=json.dumps({
                'name': 'Goku',
                'email': 'goku@dragonball.com',
                'password': 'freeza_sux123',
                'birthdate': '30/04/1994'
            }),
            content_type='application/json'
        )

    def tearDown(self):
        # mostly used for closing files and db
        pass

    def test_was_success(self):
        self.assertEqual(self.response.status_code, 200)

    def test_has_keys(self):
        _json = json.loads(self.response.get_data(as_text=True))
        assert 'Goku' in _json['name']
        assert 'goku@dragonball.com' in _json['email']
        assert 'freeza_sux123' in _json['password']
        assert '30/04/1994' in _json['birthdate']


if __name__ == '__main__':
    unittest.main()
