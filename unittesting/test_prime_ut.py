import unittest

from prime import *

class Prime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(13))

if __name__ == '__main__':
    import unittest; unittest.TestCase.run = lambda self,*args,**kw: unittest.TestCase.debug(self)
    unittest.main()
