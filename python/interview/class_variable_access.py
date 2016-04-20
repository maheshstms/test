#!/usr/bin/env python


class A():
    success = 10

print A.success
A.success = 20
a1 = A()
a2 = A()
a1.success = 30
a2.success = 40
print a1.success
print a2.success
print A.success

# Output:
# 10
# 30
# 40
# 20
# Explained:
# No complexity, just to show class variables can be accessed without objects
