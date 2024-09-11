import hw2_debugging
import pytest

array1 = [8,6,2,4,1,9,10]
array2 = [18,2,23,21,15,9,110]
array3 = [81,62,23,44,15,93,10]

def testcase1():
  assert hw2_debugging.mergeSort(array1) == [1,2,4,6,8,9,10]
def testcase2():
  assert hw2_debugging.mergeSort(array2) == [2,9,15,18,21,23,110]
def testcase3():
  assert hw2_debugging.mergeSort(array3) == [10,15,23,44,62,81,93]
