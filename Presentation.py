import string
import time
from timeit import Timer
import sys
import re

sys.setrecursionlimit(8301220)
#print(sys.getrecursionlimit())
returnValue = []
wholeFile = open("shakespeare-complete-works.txt").read().split()
shakespearWithout = []
startAll = 0



def removeSymbolsToLowercase(myFile):
    for word in myFile:
        word = re.sub('[^a-z\ \']+', " ", word)
        if((' ' in word) == True):
            wordSplits = word.split()
            for splits in wordSplits:
                shakespearWithout.append(splits.lower())
        else:
            shakespearWithout.append(word.lower())

def removeSymbolsToLowercase2(myFile):
    for word in myFile:
            if(word.isalpha()):
                shakespearWithout.append(word.lower())


def resetList():
    print("__________________________________________________")
    print("                                                  ")
    print("Reading from file")
    removeSymbolsToLowercase(wholeFile)
    #print(len(shakespearWithout))

def insertionSort(myList, printIt):
    start = time.time()
    print("Sorting", len(myList), "words with InsertionSort")
    n = len(myList)
    for i in range(1,n):
        key = myList[i]
        left = (i - 1)
        while (left > -1) and (myList[left] > key):
            myList[left+1] = myList[left]
            left = left - 1
        myList[left+1] = key
    if(printIt):
        print(myList)
    print("InsertionSort:", float("{0:.4f}".format(time.time()-start)), "seconds")

def selectionSort(myList, printIt):
    start = time.time()
    print("Sorting", len(myList), "words with SelectionSort")
    for fillslot in range(len(myList)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if myList[location]>myList[positionOfMax]:
                   positionOfMax = location

           temp = myList[fillslot]
           myList[fillslot] = myList[positionOfMax]
           myList[positionOfMax] = temp
    if(printIt):
        print(myList)
    print("SelectionSort:", float("{0:.4f}".format(time.time()-start)), "seconds")

def mergeSort(myList, printIt):
    if len( myList )>1:
        mid = len(myList)//2
        lefthalf = myList[:mid]
        rightHalf = myList[mid:]

        mergeSort(lefthalf, False)
        mergeSort(rightHalf, False)

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

    if(printIt):
        print(myList)

def quickSort(myList, printIt):
    print("Sorting", len(myList), "words with QuickSort")
    def quicksort(myList, printIt):
       quickSortHelper(myList,0,len(myList)-1, printIt)
    def quickSortHelper(myList,first,last, printIt):
       if first<last:

           splitpoint = partition(myList,first,last,printIt)

           quickSortHelper(myList,first,splitpoint-1, printIt)
           quickSortHelper(myList,splitpoint+1,last, printIt)
    def partition(myList,first,last,printIt):
       pivotvalue = myList[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and myList[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while myList[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = myList[leftmark]
               myList[leftmark] = myList[rightmark]
               myList[rightmark] = temp

       temp = myList[first]
       myList[first] = myList[rightmark]
       myList[rightmark] = temp


       return rightmark
    quicksort(myList, printIt)
    if(printIt):
        print(myList)

def heapSort(myList, printIt):
    print("Sorting", len(myList), "words with HeapSort")
    def heapsort(myList, printIt):
        heapify(myList, len(myList), printIt)
        end = len(myList)-1
        while end > 0:
            myList[end], myList[0] = myList[0], myList[end]
            end -= 1
            sift_down(myList, 0, end, printIt)
    def heapify(myList, count, printIt):
        start = int((count-2)/2)
        while start >= 0:
            sift_down(myList, start, count-1, printIt)
            start -= 1
    def sift_down(myList, start, end, printIt):
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
    heapsort(myList, printIt)
    print(printIt)
    if(printIt):
        print(myList)


def algorithmSelection(number, size, printIt):
    resetList()

    if(number == 1):
        insertionSort(shakespearWithout[:size], printIt)
    if(number == 2):
        selectionSort(shakespearWithout[:size], printIt)
    if(number == 3):
        start = time.time()
        print("Sorting", size, "words with MergeSort")
        mergeSort(shakespearWithout[:size], printIt)
        print("MergeSort runtime:", float("{0:.4f}".format(time.time()-start)), "seconds")
    if(number == 4):
        start = time.time()
        quickSort(shakespearWithout[:size], printIt)
        print("QuickSort runtime:", float("{0:.4f}".format(time.time()-start)), "seconds")
    if(number == 5):
        start = time.time()
        heapSort(shakespearWithout[:size], printIt)
        print("HeapSort runtime:", float("{0:.4f}".format(time.time()-start)), "seconds")
    if(number == 6):

        insertionSort(shakespearWithout[:size], printIt)
        resetList()
        selectionSort(shakespearWithout[:size], printIt)
        resetList()
        start = time.time()
        print("Sorting", size, "words with MergeSort")
        mergeSort(shakespearWithout[:size], printIt)
        print("MergeSort runtime:", float("{0:.4f}".format(time.time()-start)), "seconds")
        resetList()
        start = time.time()
        quickSort(shakespearWithout[:size], printIt)
        print("QuickSort time:", float("{0:.4f}".format(time.time()-start)), "seconds")
        resetList()
        start = time.time()
        heapSort(shakespearWithout[:size], printIt)
        print("HeapSort time:", float("{0:.4f}".format(time.time()-start)), "seconds")



def params(runNumber):
    if(runNumber == 1 or runNumber == 0):
        if(runNumber == 0):
            print("Enter 1 for InsertionSort")
            print("Enter 2 for SelectionSort")
            print("Enter 3 for MergeSort")
            print("Enter 4 for QuickSort")
            print("Enter 5 for HeapSort")
            print("Enter 6 for ALL")
            print("________________________________________________")
        try:
            sort = int(sys.stdin.readline())
        except ValueError:
            print("Has to be Integer between 1 and 6")
            params(1)
        if(sort < 7 and sort > 0):
            param1 = sort
            returnValue.append(param1)
            runNumber = 2
        else:
            params(1)
    if(runNumber == 2):
        print("________________________________________________")
        print("how many words do you want to sort?")
        print("Has to be a number between 1 and 830122")
        try:
            words = int(sys.stdin.readline())
        except ValueError:
            params(2)
        print("________________________________________________")
        if(words < 830123 and words > 0):
                param2 = words
                returnValue.append(param2)
                params(3)
        else:
            params(2)
    if(runNumber == 3):
        print("Do you want to print the sorted words?")
        print("Continue or 1 for Prints")
        print("________________________________________________")
        try:
            printToTerminal = sys.stdin.readline()
            if(int(printToTerminal) == 1):
                returnValue.append(True)
                print("________________________________________________")
        except ValueError:
            print(ValueError)
            returnValue.append(False)




def run():
    params(0)

    algorithmSelection(returnValue[0],returnValue[1],returnValue[2])
    print("________________________________________________")


run()
print("________________________________________________")
print("Do you want to run again?")
print("Continue, 0 to exit")
try:
    go = sys.stdin.readline()
    if(int(go) == 0):
        sys.exit()
    else:
        returnValue = []
        go = 1
        run()
except ValueError:
    go = 1
    print(ValueError)
    returnValue = []
    run()
