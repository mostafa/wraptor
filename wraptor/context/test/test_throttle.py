import time

from wraptor.context import throttle

def test_basic():
    arr = []
    t = throttle(.1)

    with t as throttler:
        if throttler:
            arr.append(1)
    with t as throttler:
        if throttler:
            arr.append(1)
    time.sleep(.2)
    with t as throttler:
        if throttler:
            arr.append(1)

    assert arr == [1, 1]
