def bubble_sort(array):
    for i in range(len(array), 0, -1):
        aux = False
        for j in range(0, i - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                aux = True
        if not aux:
            break

def insertion_sort(array):
    for p in range(0, len(array)):
        current_element = array[p]
        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1
        array[p] = current_element

def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            item = array[i]
            j = i
            while j >= gap and array[j - gap] > item:
                array[j] = array[j - gap]
                j -= gap
            array[j] = item
        gap //= 2
    return array

def merge_sort(array):
    sort_half(array, 0, len(array) - 1)
def sort_half(array, start, end):
    if start >= end:
        return
    middle = (start + end) // 2
    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)
    merge(array, start, end)
def merge(array, start, end):
    array[start: end + 1] = sorted(array[start: end + 1])

def quick_sort(array):
    if len(array) <= 1:
        return array
    less     = []
    greater  = []
    midpoint = int(len(array)/2)
    pivot    = array[midpoint]
    array    = array[:midpoint] + array[midpoint+1:]
    for item in array:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
    return (quick_sort(less) + [pivot] + quick_sort(greater))
