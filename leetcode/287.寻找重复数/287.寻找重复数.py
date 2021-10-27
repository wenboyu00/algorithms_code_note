from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        快慢指针 类似链表有环
        通过用 nums[i]和下表[i] 做映射形成，链表效果用快慢指针的方法找到存在环，再找到环入口。
         1.数组中有一个重复的整数 <==> 链表中存在环
         2.找到数组中的重复整数 <==> 找到链表的环入口
        slow = slow.next ==> slow = nums[slow]
        fast = fast.next.next ==> fast = nums[nums[fast]]
        """
        # 找到环存在
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 找到环入口
        slow = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
