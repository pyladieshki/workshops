import unittest
from determine_nth_bit.n_bit import get_bit
import random

class TestNBit(unittest.TestCase):

	def test_bit_4(self):
		a = get_bit(0b11110000, 4)
		self.assertFalse(a)
		b = get_bit(0b11111000, 4)
		self.assertTrue(b)

	def test_result_is_boolean(self):
		result = get_bit(0b10000000, 1)
		self.assertIsInstance(result, bool)

	def test_1_is_not_0(self):
		a = get_bit(0b10000010, 1)
		b = get_bit(0b10000010, 2)
		c = get_bit(0b10000010, 3)
		d = get_bit(0b10000010, 3)
		self.assertNotEqual(a, b)
		self.assertEqual(c, d)

	def test_always_0_or_1(self):
		rand_num = round(random.random() * 1000)
		last_bit = get_bit(rand_num, 1)
		self.assertTrue(0<=last_bit<=1)
		self.assertIsInstance(last_bit, int)


if __name__ == '__main__':
    unittest.main()