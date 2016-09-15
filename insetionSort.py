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

