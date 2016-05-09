
# 0(n2)
# stop if the lst is sorted
def bubble_sort(lst):
    exchanges = True
    passnum = len(lst) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                exchanges = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        passnum = passnum - 1

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
