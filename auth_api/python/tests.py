import unittest
from methods import Token, Restricted
from unittest import TestCase

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token1(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))

    def test_generate_token2(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZWRpdG9yIn0.4Km_GrMrTIX2xFMjQcrGP9VDhC9jFsnFCjxvBO8Wgio', self.convert.generate_token('noadmin', 'noPow3r'))

    def test_generate_token3(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidmlld2VyIn0.l7pxJXYHlJdtI9RME2UesMzuVjqf-RtzQeLTHomo_Ic', self.convert.generate_token('bob', 'thisIsNotAPasswordBob'))
        
    def test_generate_token4(self):
        with self.assertRaises(Exception) as context :
            self.convert.generate_token('user', 'noAccess')
        self.assertEqual(str(context.exception), 
            "403 Forbidden: You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.")

    def test_access_data1(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))

    def test_access_data2(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZWRpdG9yIn0.4Km_GrMrTIX2xFMjQcrGP9VDhC9jFsnFCjxvBO8Wgio'))

    def test_access_data3(self):
        self.assertEqual('Restricted', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidmlld2VyIn0.l7pxJXYHlJdtI9RME2UesMzuVjqf-RtzQeLTHomo_Ic'))

if __name__ == '__main__':
    unittest.main()
