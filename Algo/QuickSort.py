def quicksort(a, left, right):
    if left > right:
        return -1
    pivot = a[left]
    i = left
    j = right
    while i != j:
        while a[j] >= pivot and i < j:
            j -= 1
        while a[i] <= pivot and i < j:
            i += 1
        a[i], a[j] = a[j], a[i]
    a[left], a[i] = a[i], a[left]
    quicksort(a, left, i - 1)
    quicksort(a, i + 1, right)
    return a


def qs1(nums, left, right):
    if left >= right:
        return
    idx = right
    nums[idx], nums[right] = nums[right], nums[idx]
    pivot = nums[right]
    pos = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    nums[pos], nums[right] = nums[right], nums[pos]
    qs1(nums, left, pos - 1)
    qs1(nums, pos + 1, right)
    return nums


a = [6, 1, 100, 32, 22, 2, 6, 321, 25, 99, 54, 33, 11, 54, 23, 1, 5]
print qs1(a, 0, len(a) - 1)
