# Merge mergeable[lo .. mid] (sorted subarray) with mergeable[mid+1 .. hi] (sorted subarray) using aux[lo .. hi]


def _merge(mergeable, lo, mid, hi):

    mid = lo + int((hi - lo) / 2)

    _aux = []
    # Copy to aux[]
    for k in range(lo, hi + 1):
        _aux[k] = mergeable[k]

    # Merge back to mergeable[]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:  # Index past left subarray max index
            mergeable[k] = _aux[j]
            j += 1
        elif j > hi:  # index past right subarray max index
            mergeable[k] = _aux[i]
            i += 1
        elif _aux[j] < _aux[i]:  # compare
            mergeable[k] = _aux[j]
            j += 1
        else:
            mergeable[k] = _aux[i]
            i += 1
    return
