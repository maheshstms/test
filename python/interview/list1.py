#!/usr/bin/env python


def f(x, l=[]):
    for i in range(x):
        l.append(i)
    print l

f(2)
f(3, [1, 2, 3])
f(3)
# Output:
# [0, 1]
# [1, 2, 3, 0, 1, 2]
# [0, 1, 0, 1, 2]
# Reason:
# The strange output is bacause, the default initialization of 'l' is done
# when it is defined and not during calling. But f(3, [1, 2, 3]) sends
# its own list so you see what you expect. f(3) uses 'l' that f(2) left.
# Solve:
# def f(x, l=None): # Used None
#    if l is None:
#        l = []
#
#    for i in range(x):
#        l.append(i)
#
#    print l
