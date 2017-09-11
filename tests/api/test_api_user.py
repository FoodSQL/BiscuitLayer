import unittest
import json
import biscuit

from mock import patch, Mock
from tests.mock.user_mock import User_Mock


def fake_user(name, email, password, birthdate):
    # Inserting mock mid-application
    return User_Mock(None, name, email, password, birthdate)


def get_fake_user(email):
    return User_Mock(None, 'Gohan', email, 'iliketurtles123', '30/04/1994')


def fake_update_user(user_id, user_name, user_email, user_password):
    user = User_Mock(None, user_name, user_email, user_password, None)
    user._id = user_id
    return user

class UpdateUserAPITestCase(unittest.TestCase):

    @patch('biscuit.biscuit.update_user', side_effect=fake_update_user)
    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()
        self.res = self.app.post(
            '/user/update',
            data=json.dumps({
                'user_id': 42,
                'user_name': 'Freeza',
                'user_email': 'freeza@dragonball.com',
                'user_password': 'goku_sux123',
                'user_birthdate': '30/04/1994',
            }),
            content_type='application/json'
        )


    def tearDown(self):
        pass


    def test_was_success_status(self):
        self.assertEquals(200, int(self.res.status_code))


    def test_basic_json_integrity(self):
        _json = json.loads(self.res.get_data(as_text=True))
        self.assertEquals(42, int(_json['user_id']))
        assert 'freeza' in str(_json['user_name']).lower()
        assert 'freeza@dragonball.com' in str(_json['user_email']).lower()


class APILoginUserTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()


    def tearDown(self):
        pass


    @patch('biscuit.biscuit.get_user', side_effect=get_fake_user)
    def test_was_success(self, mock):
        response = self.app.post(
            '/user/login',
            data=json.dumps({
                'email': 'gohan@dragonball.com',
                'password': 'iliketurtles123'
            }),
            content_type='application/json'
        )
        _json = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        assert 'gohan@dragonball' in _json['email']
        assert 'Gohan' in _json['name']


    @patch('biscuit.biscuit.get_user', side_effect=get_fake_user)
    def test_was_failure(self, mock):
        response = self.app.post(
            '/user/login',
            data=json.dumps({
                'email': 'gohan@dragonball.com',
                'password': 'ihateturtles123'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 406)
        assert b'Not acceptable' in response.data


    def test_get_was_rejected(self):
        response = self.app.get('/user/login')
        self.assertEqual(response.status_code, 405)


class APICreateUserTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
