from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        sort = []
        while i < m or j < n:
            if i == m:
                sort.append(nums2[j])
                j += 1
            elif j == n:
                sort.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                sort.append(nums1[i])
                i += 1
            else:
                sort.append(nums2[j])
                j += 1
        # 直接赋值是改变对象引用，要[:]来改变list对象中的值
        nums1[:] = sort


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
