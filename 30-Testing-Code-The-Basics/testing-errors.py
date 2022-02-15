import unittest

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
        # fails b/c no ZeroDivisionError raised
        # self.assertRaises(ZeroDivisionError, divide, 10, 5)

    # like using
    # with open("filename.txt", r) as file:
    def test_divide_another_way(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_raises_name_error(self):
        with self.assertRaises(NameError):
            non_existent_function(1, 2)
        

if __name__ == "__main__":
    unittest.main()