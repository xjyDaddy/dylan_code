#Date:2018/5/4
#Author:dylan_xi
#Desc:a simple quick_sort algorithm demo

def partition(array ,begin = None , end = None):
    #if section have one less element return 
    if begin >= end:
        return
    baseValue = array[begin]
    guardLeft = begin
    guardRight = end
    while(guardLeft < guardRight):
        while(array[guardRight] >= baseValue and guardRight > guardLeft):
            guardRight = guardRight - 1
        while(array[guardLeft] <= baseValue and guardRight > guardLeft):
            guardLeft = guardLeft + 1
        array[guardLeft],array[guardRight] = array[guardRight],array[guardLeft]
    array[begin] , array[guardLeft] = array[guardLeft] , array[begin]
    return guardLeft

def quick_sort(array , begin , end):
    if begin >= end:
        return
    partitionIndex = partition(array , begin , end) 
    #sort left
    quick_sort(array , begin , partitionIndex-1)
    #sort right
    quick_sort(array , partitionIndex+1 , end)

#test partition
array1 = [3,5,1,2,6]
assert(partition(array1 , 0 ,4) == 2)
assert(array1 == [1,2,3,5,6])        

#test quick_sort
array2 = [3,9,4,2,5,1,8,7]
quick_sort(array2 , 0 , len(array2)-1)
assert(array2 == [1,2,3,4,5,7,8,9])

array3 = [3,4,3,4,3,2,1,8]
quick_sort(array3 , 0 , len(array3)-1)
assert(array3 == [1,2,3,3,3,4,4,8])
