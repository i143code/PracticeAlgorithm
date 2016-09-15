#If it is the first element, it is already sorted. return 1;
# Pick next element
#Compare with all elements in the sorted sub-list
#Shift all the elements in the sorted sub-list that is greater than the value to be sorted
#Insert the value
# Repeat until list is sorted


def insertionSort(array):
    for i in range(1,len(array)):
        position = i
        currentPostion = array[i]

        while i > 0 and array[position -1] > currentPostion:
            array[position] = array[position-1]
            position = position -1
            array[position] = currentPostion


arr= [1,2,3,6,8,4]
insertionSort(arr)

