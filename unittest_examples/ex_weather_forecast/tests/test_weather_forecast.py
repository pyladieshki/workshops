#!/usr/bin/python3
import unittest
from ex_weather_forecast.weather_forecast import temp_now, how_does_it_feel

# NOTE: all assert methods can be found here:
# https://docs.python.org/3.5/library/unittest.html#assert-methods

class TestWeatherForecast(unittest.TestCase):

    def setUp(self):
        pass

    def test_temp_is_int(self):
        temp = temp_now()
        self.assertIsInstance(temp, int)

    def test_feeling_is_str(self):
        temp = temp_now()
        feeling = how_does_it_feel(temp)
        self.assertIsInstance(feeling, str)

    def test_it_is_cold(self):
        feeling = how_does_it_feel(-10)
        self.assertEqual(feeling, 'Brrrr!')
        self.assertNotEqual(feeling, 'Freaking Cold!')
        self.assertNotEqual(feeling, 'It is freaking HOT!')

    # Write similar tests for temps > 10, and between 0 and 10

    # Write another test for testing of whether it will be colder or warmer
    # or the same temperature in 3 hours

    # Write one or several tests for the function that returns
    # the temperature in 3 hours

if __name__ == '__main__':
    unittest.main()