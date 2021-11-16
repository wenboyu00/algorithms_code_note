from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        先合并，然后找到中位数
        时间复杂度 N(n+m)
        """
        new = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
        if i < n1:
            new.extend(nums1[i:])
        if j < n2:
            new.extend(nums2[j:])
        n = len(new)
        if n % 2 == 1:
            return new[n // 2]
        else:
            return (new[n // 2] + new[n // 2 - 1]) / 2

    def findMedianSortedArraysLogm(self, nums1: List[int], nums2: List[int]) -> float:
        """
        划分数组法
        合并后的数组中值左半边由nums1和nums2左半边贡献元素，找到num1分割的位置也就找到nums2
        分割线的条件是：分割线左边<=右边
            - L1 <= R2
            - L2 <= R1

        """
        len_1, len_2 = len(nums1), len(nums2)
        if len_1 > len_2:
            return self.findMedianSortedArraysLogm(nums2, nums1)
        if len_1 == 0:
            return nums2[(len_2 - 1) // 2] + nums2[len_2 // 2] / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    print(Solution().findMedianSortedArraysLogm(nums1, nums2))
