def heapsort(myList):
    heapify(myList, len(myList))
    end = len(myList)-1
    while end > 0:
        myList[end], myList[0] = myList[0], myList[end]
        end -= 1
        sift_down(myList, 0, end)

def heapify(myList, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(myList, start, count-1)
        start -= 1

def sift_down(myList, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if myList[swap] < myList[child]:
            swap = child
        if (child + 1) <= end and myList[swap] < myList[child+1]:
            swap = child+1
        if swap != root:
            myList[root], myList[swap] = myList[swap], myList[root]
            root = swap
        else:
            return


array = [6,7,3,16,89,5,6,1,2]
heapsort(array)
print(array)
