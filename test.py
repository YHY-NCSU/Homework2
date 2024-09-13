import hw2_debugging

array1 = [8,6,2,4,1,9,10]
array2 = [18,2,23,21,15,9,110]
array3 = [81,62,23,44,15,93,10]

def testcase1():
  assert hw2_debugging.mergeSort(array1) == array1.sort()
def testcase2():
  assert hw2_debugging.mergeSort(array2) == array2.sort()
def testcase3():
  assert hw2_debugging.mergeSort(array3) == array3.sort()
