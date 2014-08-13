
def perm(it, r=None):
    """Permutations of iterator `it` of length `r`"""

    if r == 0:
        # Nothing returned
        return

    it = tuple(it)
    if r is None:
        r = len(it)

    results = [ ]

    if r == 1:
        for first in it:
            yield (first, )
        return

    for i in range(len(it)):
        first = it[i]
        rest = it[:i] + it[i+1:]
        for order in perm(rest, r-1):
            #print(' '*r, first, order)
            yield (first,) + order
