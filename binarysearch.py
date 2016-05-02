# binary search
import test

def binarySearch(mylist, item):
    first = 0
    last = len(mylist) - 1
    found = False
  
    when first <= last and not found:
        mid = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

# recursive binarySearch
def binarySearchR(mylist, item):
    if len(mylist) == 0:
        return False
    else:
        mid = len(mylist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < mylist[mid]:
                return binarySearchR(mylist[:midpoint+1], item)
            else:
                return binarySearchR(mylist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))