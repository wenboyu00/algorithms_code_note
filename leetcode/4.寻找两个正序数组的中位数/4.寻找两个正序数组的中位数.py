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
        合并后的数组中值左半边由nums1和nums2左半边贡献元素，找到num1分割的位置cut1，也就找到cut2，就可以确定中值的位置
        分割线的条件是：分割线左边<=右边
            - L1 <= R2
            - L2 <= R1
            - 因为是数组有序的，所以分割线左右的4个数字也是有序的。
        cut1是num1分割线位置，通过二分法求出
        cut2是num2分割线位置，等于(总元素个数+1的中值) - cut1
            - 总元素个数+1/2 是因为这样可以方便求助总元素个数为奇数时的中值
        比较l1和r2关系l2和r1关系来更新cut1位置
        满足条件时
            - 如果总元素为奇数，中值= l1和l2最大值
            - 如果总元素为偶数，中值= 左半边最大值+右半边最小值的二分之一
        """
        len_1, len_2 = len(nums1), len(nums2)
        if len_1 > len_2:
            return self.findMedianSortedArraysLogm(nums2, nums1)
        if len_1 == 0:
            return (nums2[(len_2 - 1) // 2] + nums2[len_2 // 2]) / 2
        len_all = len_1 + len_2
        # 只对nums1进行二叉查找
        left1, right1 = 0, len_1
        while left1 <= right1:
            # nums1分割线左边的个数(中值)，nums1中点位置
            cut1 = (left1 + right1) // 2
            # nums2分割线左边的个数(中值)，(总长度+1)/2中点位置 - cut1个数
            # len_all+1，如果总元素个数为奇数，直接返回分割线左边元素。所以左半边要比右半边多出一个
            cut2 = (len_all + 1) // 2 - cut1
            # 边界值判断，如果左半边超过边界值就等于 最小值
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            # 如果右半边超过边界就等于 最大值
            r1 = float('inf') if cut1 == len_1 else nums1[cut1]
            r2 = float('inf') if cut2 == len_2 else nums2[cut2]
            # 二分法
            # l1>r2说明l1过大，需要缩小，新的右边界等于 cut1(中值) -1
            if l1 > r2:
                right1 = cut1 - 1
            # l2>r1说明r1过小，需要增大，新的左边界等于 cut1+1
            elif l2 > r1:
                left1 = cut1 + 1
            # 满足条件 l1<=r2 and l2<=r1，找到nums1切割线
            else:
                # 偶数情况 = 左半边的较大者和右半边的较小值相加/2
                if len_all % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                # 奇数情况 = 左半边的较大者
                else:
                    return max(l1, l2)
        return -1


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    nums1 = [4, 5]
    nums2 = [1, 2, 3]
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    print(Solution().findMedianSortedArraysLogm(nums1, nums2))
