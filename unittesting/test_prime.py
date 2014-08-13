from nose.tools import *

from prime import *

def test_is_prime():
    assert_true(is_prime(2))
    assert_true(is_prime(3))
    assert_false(is_prime(4))
    assert_true(is_prime(5))
    assert_false(is_prime(9))
    assert_false(is_prime(10))
    assert_true(is_prime(13))
