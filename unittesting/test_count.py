from nose.tools import *

from count import *

def test_count():

    # Count of an empty iterator should return an empty dict.
    # [0] -> {}
    assert_dict_equal(count([]), {})

    # [1] -> {1: 1}
