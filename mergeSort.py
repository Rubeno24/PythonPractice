def mergeSort(array):
    if len(array) > 1:
        rightArray = array[0:len(array)//2]
        leftArray = array[len(array)//2:len(array)]
        
        mergeSort(leftArray)
        mergeSort(rightArray)
        
        leftIndex = 0
        rightIndex = 0
        mergedIndex = 0

        while leftIndex < len(leftArray) and rightIndex < len(rightArray):
            if leftArray[leftIndex] < rightArray[rightIndex]:
                array[mergedIndex] = leftArray[leftIndex]
                leftIndex += 1
                mergedIndex+=1
            else:
                array[mergedIndex] = rightArray[rightIndex]
                rightIndex += 1
                mergedIndex += 1

        while leftIndex < len(leftArray):
            array[mergedIndex] = leftArray[leftIndex]
            leftIndex += 1
            mergedIndex += 1

        while rightIndex < len(rightArray):
            array[mergedIndex] = rightArray[rightIndex]
            rightIndex += 1
            mergedIndex += 1

arr = [134, 23, 45, 23, 24, 4, 54, 23, 5, 4, 5, 4]
mergeSort(arr)
print(arr)
