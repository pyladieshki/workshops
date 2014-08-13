import unittest

import fib

class TestFib(unittest.TestCase):
    # Define which function we will test.
    fib = staticmethod(fib.fib1)

    def test(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(2), 1)
        self.assertEqual(self.fib(3), 2)
        self.assertEqual(self.fib(4), 3)
        self.assertEqual(self.fib(5), 5)

# Use inheritance to simplify the testing of fib2.
class TestFib2(TestFib):
    # All the same tests as TestFib1, but different function to test.
    fib = staticmethod(fib.fib2)



# This boilerplate allows us to run using unittest.
if __name__ == '__main__':
    unittest.main()
