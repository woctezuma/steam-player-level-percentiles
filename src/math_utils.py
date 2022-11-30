import math
from functools import reduce


def lcm_pair(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_list(l):
    return reduce(lcm_pair, l)


def compute_denominator(x):
    return x.as_integer_ratio()[1]


def compute_denominators_from_dict(d, max_input_value=100):
    l = []
    for p in d.values():
        q = max_input_value - p
        l.extend((compute_denominator(p), compute_denominator(q)))
    return lcm_list(l)
