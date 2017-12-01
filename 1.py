import unittest

def solve(s, match):
    l = [int(a) for a in s]

    total = 0
    for i,a in enumerate(l):
        if a == match(l, i):
            total += a
    return total

def first(s):
    return solve(s, lambda l, i: l[(i+1) % len(l)])

def second(s):
    return solve(s, lambda l, i: l[(i + len(l)/2) % len(l)])

import sys
inp = sys.stdin.read().strip()
print first(inp)
print second(inp)
