def quick_sort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quick_sort(nums, left, index - 1)
        quick_sort(nums, index + 1, right)


def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    return i


if __name__ == '__main__':
    arr = [1, 3, 2, 2, 0]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
