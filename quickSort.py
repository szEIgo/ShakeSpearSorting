def qsort(list):
    if list == []:
        return []
    pivot = list[0]
    l = qsort([x for x in list[1:] if x < pivot])
    u = qsort([x for x in list[1:] if x >= pivot])
    return l + [pivot] + u


array = [6,7,3,16,89,5,6,1,2]
qsort(array)
print(array)
