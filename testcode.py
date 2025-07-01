import unittest
from sample import sms

class TestApp(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sms(),'Hello World')

if __name__ == "__main__":
    unittest.main()
