array = [6,7,3,16,89,5,6,2, 1, 5, 6,2 ,7,2,1]
array2 = 0

print(array)
def doSelectionSort( myList):
    for fillslot in range(len(myList)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if myList[location]>myList[positionOfMax]:
                   positionOfMax = location

           temp = myList[fillslot]
           myList[fillslot] = myList[positionOfMax]
           myList[positionOfMax] = temp
    return myList

array2 = doSelectionSort(array)
print(array2)
