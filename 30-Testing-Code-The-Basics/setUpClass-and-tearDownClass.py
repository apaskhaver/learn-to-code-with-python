import unittest

class TestOperations(unittest.TestCase):
    def setUp(self):
        print("This will run before each test.")

    def tearDown(self):
        print("This will run after each test.")

    @classmethod
    def setUpClass(cls):
        print("This will run once before the test suite runs.")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after the test suite runs.")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()