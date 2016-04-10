#!/usr/bin/python3
import sys
if sys.version_info[0] < 3:
	sys.exit('Python 3 is required')
import io
from pprint import pprint

# TODO: handle Unicode characters correctly
def is_ascii_letter(letter):
	return letter.isalnum()

def handle_word(freqs, word):
	"""Adds word to freqs dictionary, increasing freqs[word] by 1
	"""
	# TODO: 'canonicalize' word before adding to freqs, e. g. convert to lowercase
	if word:
		if word in freqs:
			freqs[word] += 1
		else:
			freqs[word] = 1

def analyze(s, is_letter=None):
	"""Returns a dictionary with words as keys and their number of occurrences
	in string s as values.
	"""
	if is_letter is None:
		is_letter = is_ascii_letter
	freqs = {}
	word = ''
	for letter in s:
		if is_letter(letter):
			word += letter
		else:
			handle_word(freqs, word)
			word = ''
	handle_word(freqs, word)
	return freqs

def as_array(freqs):
	"""Converts freqs dictionary of the form {word: freq, ...} to an array of tuples
	of the form [(word, freq), ...], sorted in increasing order by freq
	"""
	# TODO: add percentage of each word as the 3rd element of the tuple
	arr = sorted(freqs, key=lambda word: freqs[word])
	return [(word, freqs[word]) for word in arr]

def print_freqs_arr(freqs):
	for word, freq in freqs:
		print(word + ': ' + str(freq)) 

def main():
	string = sys.stdin.read(None)
	freqs = analyze(string)
	#pprint(freqs)
	freqs_arr = as_array(freqs)
	print_freqs_arr(freqs_arr)

if __name__ == '__main__':
	main()
