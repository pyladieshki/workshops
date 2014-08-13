import unittest

from perm import *

class Perm(unittest.TestCase):
    def test_perm(self):

        # Permutations of empty sequence is emty
        self.assertSetEqual(set(perm([])),
                            set([])  )

        # Permutations of length-1 sequence is itself
        self.assertSetEqual(set(perm([1])),
                            set([(1,)])  )

        # Permutations of length-2 sequence:
        self.assertSetEqual(set(perm([1, 2])),
                            set([(1,2), (2,1)])  )

        # Permutations of length-3 sequence:
        self.assertSetEqual(set(perm([1, 2, 3])),
                            set([(1,2,3),(1,3,2),(2,1,3),(2,3,1),
                                 (3,1,2),(3,2,1)])  )


        # Test shorter permutations

        # Zero element permutation of 2-list
        self.assertSetEqual(set(perm([1, ], 0)),
                            set([])  )

        self.assertSetEqual(set(perm([1, 2], 1)),
                            set([(1,), (2,)])  )

        self.assertSetEqual(set(perm([1, 2, 3], 2)),
                            set([(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)])  )

        self.assertSetEqual(set(perm([1, 2, 3, 4], 2)),
                            set([(1,2),(1,3),(1,4),
                                 (2,1),(2,3),(2,4),
                                 (3,1),(3,2),(3,4),
                                 (4,1),(4,2),(4,3)])  )

if __name__ == '__main__':
    unittest.main()
