# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
#
#
#
#  限制：
#
#  1 <= 数组长度 <= 50000
#
#
#
#  注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
#
#
#  Related Topics 位运算 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        count = dict()
        half = len(nums) // 2
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for k, v in count.items():
            if v > half:
                return k
        return -1
# leetcode submit region end(Prohibit modification and deletion)
