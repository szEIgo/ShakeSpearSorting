def mergeSort( myList):
    if len( myList )>1:
        mid = len(myList)//2
        lefthalf = myList[:mid]
        rightHalf = myList[mid:]

        mergeSort(lefthalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(rightHalf):
            if (lefthalf[i] < rightHalf[j]):
                myList[k] = lefthalf[i]
                i = i + 1
            else:
                myList[k] = rightHalf[j]
                j = j + 1

            k = k + 1

        while i < len(lefthalf):
            myList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            myList[k] = rightHalf[j]
            j = j + 1
            k = k + 1
array = [6,7,3,16,89,5,6,1,2]

print(len(array) // 2)    
print(array)
mergeSort(array)
print(array)
