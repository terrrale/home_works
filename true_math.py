from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


res1 = divide(3, 4)
res2 = divide(3, 0)