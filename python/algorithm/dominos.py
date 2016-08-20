#!/usr/bin/env python

tc = int(raw_input())
tcl = [[0 for x in range(2)] for y in range(tc)]
for testCase in range(tc):
    count = int(raw_input())
    tcl[testCase][0] = list(raw_input())
    tcl[testCase][1] = list(raw_input())

for testCase in range(tc):
    if (tcl[testCase][0].count('0') + tcl[testCase][1].count('0')) % 2 is 0:
        print "YES"
    else:
        print "NO"
