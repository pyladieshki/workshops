#!/usr/bin/python3
import unittest
from freq_analysis import is_ascii_letter, handle_word, analyze, as_array

class TestFrequencyAnalysis(unittest.TestCase):
	def test_is_ascii_letter(self):
		self.assertTrue(is_ascii_letter('a'))
		self.assertTrue(is_ascii_letter('Z'))
		self.assertFalse(is_ascii_letter('/'))
		self.assertFalse(is_ascii_letter('_'))
	
	def test_handle_word(self):
		freqs = {}
		handle_word(freqs, 'hello')
		self.assertEqual(freqs, {'hello': 1})
		handle_word(freqs, 'hello')
		self.assertEqual(freqs, {'hello': 2})
		handle_word(freqs, 'world')
		self.assertEqual(freqs, {'hello': 2, 'world': 1})

	def test_analyze(self):
		res = {'a': 2, 'b': 1}
		self.assertEqual(res, analyze('a b a'))
		res = {'hello': 3, 'world': 1}
		self.assertEqual(res, analyze('/\nhello[^]hello}|!#&\nworld-hello)(*'))

	def test_as_array(self):
		inp = {'a': 2, 'b': 1}
		res = [('b', 1), ('a', 2)]
		self.assertEqual(res, as_array(inp))
		inp = {'hello': 3, 'world': 1, 'hei': 2, 'maailma': 5}
		res = [('world', 1), ('hei', 2), ('hello', 3), ('maailma', 5)]
		self.assertEqual(res, as_array(inp))

if __name__ == '__main__':
	unittest.main()
