import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "g"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 3)

# only if this is the executing file,
# run the main file. Will execute tests.
if __name__ == "__main__":
    unittest.main()

# will get FF
# b/c test_split and test_count both fail