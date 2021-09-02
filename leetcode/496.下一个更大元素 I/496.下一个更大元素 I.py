from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. 找到nums2值的下一个最大值
            - map{num: 下一个最大值}关系， stack 单调栈
            - 倒叙循环nums2, 通过栈获得每个值的下个一个最大值，
            - 保存num和下一个最大值的关系
        2. 通过nums1值和map获得值的下一个最大值
        """
        # {num2的值：下一个最大的值}，用于nums1的值和nums2值对应
        res_map = {}
        # 单调栈
        stack = []
        # 最后向前遍历nums2
        for i in range(len(nums2) - 1, -1, -1):
            # 当前num2的值大于 栈顶的值 就弹出栈顶
            while stack and nums2[i] > nums2[stack[-1]]:
                stack.pop()
            # 如果栈为空，说没有下一个最大值
            if stack:
                res_map[nums2[i]] = nums2[stack[-1]]
            else:
                res_map[nums2[i]] = -1
            # 把当前值加入进去
            stack.append(i)
        # 遍历num1获得num的最大值
        res = []
        for num in nums1:
            res.append(res_map.get(num, -1))
        return res


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = Solution().nextGreaterElement(nums1, nums2)
    print(result)
