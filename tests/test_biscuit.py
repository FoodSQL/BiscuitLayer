import os
import biscuit
import unittest
import tempfile


class BiscuitTestCase(unittest.TestCase):

    def setUp(self):
        biscuit.app.testing = True
        self.app = biscuit.app.test_client()

    def tearDown(self):
        # mostly used for closing files and db
        pass

    def test_home_response(self):
        response = self.app.get('/')
        assert b'Invalid page' in response.data
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
