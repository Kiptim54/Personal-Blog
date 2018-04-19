import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        '''
        sets up password before tests are run
        '''
        self.new_user = User(password = 'koko')

    def test_password_setter(self):
        '''
        ensures that when generating password the 
        password if not blank
        '''
        self.assertTrue(self.new_user.password is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        test to ensure password_hash_checker works
        '''
        self.assertTrue(self.new_user.verify_password('koko'))
