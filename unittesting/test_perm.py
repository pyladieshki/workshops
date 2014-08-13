
from nose.tools import *

from perm import *


def test_perm():

    # Permutations of empty sequence is emty
    assert_set_equal(set(perm([])),
                     set([])  )

    # Permutations of length-1 sequence is itself
    assert_set_equal(set(perm([1])),
                     set([(1,)])  )

    # Permutations of length-2 sequence:
    assert_set_equal(set(perm([1, 2])),
                     set([(1,2), (2,1)])  )

    # Permutations of length-3 sequence:
    assert_set_equal(set(perm([1, 2, 3])),
                     set([(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)])  )


    # Test shorter permutations

    # Zero element permutation of 2-list
    assert_set_equal(set(perm([1, ], 0)),
                     set([])  )

    assert_set_equal(set(perm([1, 2], 1)),
                     set([(1,), (2,)])  )

    assert_set_equal(set(perm([1, 2, 3], 2)),
                     set([(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)])  )

    assert_set_equal(set(perm([1, 2, 3, 4], 2)),
                     set([(1,2),(1,3),(1,4),
                          (2,1),(2,3),(2,4),
                          (3,1),(3,2),(3,4),
                          (4,1),(4,2),(4,3)])  )
