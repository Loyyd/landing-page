#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
a, b = s[0].split()
c = s[1].strip()

print(c)
#print(list(range(int(a), int(b) + 1)))
print([c for c in s[1]])

