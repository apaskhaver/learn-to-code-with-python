import unittest

def copy_and_add_element(values, element):
        copy = values[:]
        # copy = values
        copy.append(element)
        return copy

class TestInequality(unittest.TestCase):

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)

        self.assertEqual(result, [1, 2, 3, 4])

        # tests that a true copy was made, that
        # values remains unchanged
        self.assertNotEqual(values, [1, 2, 3, 4], 
            "The copy_and_add_element function is mutating the input. Make sure you're creating a copy.") 

    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("hello", "Hello")
        self.assertNotEqual([1, 2], [2, 1])

if __name__ == "__main__":
    unittest.main()