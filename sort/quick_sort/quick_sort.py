# 快排-递归
def quick_sort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quick_sort(nums, left, index - 1)
        quick_sort(nums, index + 1, right)


def partition(nums, left, right):
    """
    以nums[left]为比较点，使在比较点左边的数比它小，右边的数比它大
    使用左右指针, 进行循环
    - j先找到比比较点小的值，赋值给nums[i]
    - i再找到比比较点大的值，赋值给nums[j]
    循环结束后，nums[i] = 比较点。最后返回比较点的index

    分为2部分，交织进行
    - 位置交换
        pivot = nums[left]
        i, j = left, right
        # 此时i=left，相等于比pivot小的值直接覆盖了pivot的值
        nums[i] = nums[j]
        # 此时nums[i]是大于pivot的值，覆盖了之前pivot小的值
        nums[j] = nums[i]
        # 最后nums[i]= pivot, 相当于pivot在交换过程中承担了临时节点的功能
        # 区别在于，交换过程中i是动态，所以完成了 nums[i] < pivot< nums[j]
        nums[i] = pivot
    - 找到i和j位置
        # 从后向前找，直到找到一个比pivot更小的数
        while i < j and nums[j] >= pivot:
            j -= 1
        # 从前向后找，直到找到一个比pivot跟小的数
        while i < j and nums[i] <= pivot:
            i += 1
        """
    # 初始化一个比较数据(pivot:支点)
    pivot = nums[left]
    # 左右指针
    i, j = left, right
    while i < j:
        # 从后向前找，直到找到一个比pivot更小的数
        while i < j and nums[j] >= pivot:
            j -= 1
        # 将更小的数放入左边
        nums[i] = nums[j]
        # 从前向后找，直到找到一个比pivot跟小的数
        while i < j and nums[i] <= pivot:
            i += 1
        # 将更大的数放入右边
        nums[j] = nums[i]
    # 循环结束，i与j相等，比较数据放入最终位置
    nums[i] = pivot
    # 返回比较数据最终位置
    return i


def top_k_split(nums, k, left, right):
    """
    寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    """
    #
    if left < right:
        index = partition(nums, left, right)
        if index == k:
            return
        elif index < k:
            top_k_split(nums, k, index + 1, right)
        else:
            top_k_split(nums, k, left, index - 1)


def top_k_smalls(nums, k):
    """
    获得前k小的数
    """
    top_k_split(nums, k, 0, len(nums) - 1)
    return nums[:k]


def top_k_small(nums, k):
    """
    获得第k小的数
    """
    top_k_split(nums, k, 0, len(nums) - 1)
    # 右边是开区间，需要-1
    return nums[k - 1]


def top_k_larges(nums, k):
    """
    获得前K大的数
    partition是升序排列，让index左边为前n-k个小的数，则index右边为前k个大的数
    """
    n = len(nums)
    top_k_split(nums, n - k, 0, n - 1)
    return nums[n - k:]


def top_k_large(nums, k):
    """
    第k大的数
    """
    n = len(nums)
    top_k_split(nums, n - k, 0, n - 1)
    return nums[n - k]


if __name__ == '__main__':
    # 快排
    arr = [1, 3, 2, 2, 0]
    quick_sort(arr, 0, len(arr) - 1)
    print(f'快排:{arr}')
    # 前k小的数
    arr = [1, 3, 2, 3, 0, -19]
    k = 2
    print(f'列表:{arr} k:{k} 前k小的数:{top_k_smalls(arr, k)}')
    # 第k小的数
    arr = [1, 3, 2, 3, 0, -19]
    k = 3
    print(f'列表:{arr} k:{k} 第k小的数:{top_k_small(arr, k)}')
    # 前k大的数
    arr = [1, 3, -2, 3, 0, -19]
    k = 3
    print(f'列表:{arr} k:{k} 前k大的数:{top_k_larges(arr, k)}')

    arr = [1, 3, -2, 3, 0, -19]
    k = 2
    print(f'列表:{arr} k:{k} 第k大的数:{top_k_large(arr, k)}')
