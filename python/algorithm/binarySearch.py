#!/usr/bin/env python

# Function to find element
def binarySearch(sortedList, element, first=None, mid=None, last=None):
    if first is None:
        first = 0
    if mid is None:
        mid = abs(len(sortedList)/2)
    if last is None:
        last = len(sortedList) - 1

    if sortedList[mid] is element:
        return mid, sortedList[mid]

    if sortedList[first] is element:
        return first, sortedList[first]

    if sortedList[last] is element:
        return last, sortedList[last]

#    print "Start ->", element, (first, mid, last) ,(sortedList[first], sortedList[mid], sortedList[last])
    if sortedList[mid] > element:
        last = mid
        mid = abs((first+last)/2)
    else:
        first = mid
        mid = abs((first + last)/2)

#    print "Changed ->", element, (first, mid, last) ,(sortedList[first], sortedList[mid], sortedList[last])

    # TODO: No lofic to check if number is not available in the list

    if last is first:
        return None
    else:
        return binarySearch(sortedList, element, first, mid, last)




# Input sorted list
l = range(1000000)#[1, 3, 10, 15, 17, 19, 20, 21, 25, 28, 30, 31, 32, 33, 36, 38, 39, 40, 41, 50, 55, 56, 58, 60]
#print l

search = raw_input()

loc = binarySearch(l, int(search))

print loc
