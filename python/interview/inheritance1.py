#!/usr/bin/env python


class A(object):
    def start(self):
        print "I am in A start"

    def stop(self):
        print "I am in A stop"

    def pause(self):
        raise "Not implemented yet :("


class B(A):
    def start(self):
        super(B, self).start()
        print "I am in B start"


class C(A):
    def start(self):
        super(C, self).start()
        print "I am in C start"

    def stop(self):
        super(C, self).stop()
        print "I am in C stop"


class D(B, C):
    def start(self):
        super(D, self).start()
        print "I am in D start"

    def stop(self):
        super(D, self).stop()
        print "I am in D stop"


class E(B, C):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

d.start()
print "-----------------------"
e.start()
print "-----------------------"
b.stop()
print "-----------------------"
e.pause()
print "-----------------------"

# Result:
# I am in A start
# I am in C start
# I am in B start
# I am in D start
# -----------------------
# I am in A start
# I am in C start
# I am in B start
# -----------------------
# I am in A stop
# -----------------------
# Traceback (most recent call last):
#       File "./inheritance1.py", line 56, in <module>
#           e.pause()
#             File "./inheritance1.py", line 12, in pause
#                 raise "Not implemented yet :("
#             TypeError: exceptions must be old-style classes or derived ...
# Explained:
# I expected the first output to be
# I am in A start
# I am in B start
# I am in A start
# I am in C start
# I am in D start
# This is not happening because, Python prepares a
# MRO (Method Resolution Order). the oder of execution of start function
# becomes [D, B, C, A] since first line of 'start()' always calls super
# Intead printing D, it calls B, B calls C and C calls A. when printing
# A prints and cll reaches C so C prints then B later D.
# Refer the below link for details, good to read.
# https://en.wikipedia.org/wiki/C3_linearization
