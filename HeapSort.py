def heapSort(arr):
    for i in range(len(arr) / 2, -1, -1):
        heapify(arr, i, len(arr))
    length = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        length -= 1
        heapify(arr, 0, length)
    return arr


def heapify(arr, i, arrLen):
    left = i * 2 + 1
    right = i * 2 + 2
    root = i
    if left < arrLen and arr[left] < arr[root]:
        root = left
    if right < arrLen and arr[right] < arr[root]:
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, root, arrLen)


def heapSortIter(arr):
    for i in range(len(arr) / 2, -1, -1):
        heapifyIter(arr, i, len(arr) - 1)
    print arr
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapifyIter(arr, 0, i - 1)
    return arr


def heapifyIter(arr, start, end):
    root = start
    child = start * 2 + 1
    while child <= end:
        right = child + 1
        if right <= end and arr[right] < arr[child]:
            child = right
        if arr[child] < arr[root]:
            arr[child], arr[root] = arr[root], arr[child]
            root = child
            child = root * 2 + 1
        else:
            break


print heapSortIter([5, 3, 4, 1, 2])
