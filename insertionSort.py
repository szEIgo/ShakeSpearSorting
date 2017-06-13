array = [6,7,3,16,89,5,6,1,2]

n = len(array)

print(array)
print("length(n) = ",n)

steps = 0

for i in range(1,n):
    key = array[i]
    left = (i - 1)
    #print(left)
    while (left > -1) and (array[left] > key):
        array[left+1] = array[left]
        left = left - 1
        steps = steps +1
    array[left+1] = key
    1steps = steps +1

print (array)
print(steps)
