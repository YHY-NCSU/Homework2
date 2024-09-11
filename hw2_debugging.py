import rand

def mergeSort(arr):
    
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    iterator = 0
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            
            mergeArr[iterator] = leftArr[leftIndex]
            leftIndex += 1
        else:
            
            mergeArr[iterator] = rightArr[rightIndex]
            rightIndex += 1
        iterator +=1

    for i in range(rightIndex, len(rightArr)):
        mergeArr[iterator] = rightArr[i]
        iterator +=1
    for i in range(leftIndex, len(leftArr)):
        mergeArr[iterator] = leftArr[i]
        iterator +=1
    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)


