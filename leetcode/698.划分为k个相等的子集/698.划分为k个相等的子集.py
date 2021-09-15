from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k > n:
            return False
        nums_sum = sum(nums)
        # 总值%桶数 == 0 ，可以被整除才能进行元素和查找
        if nums_sum % k != 0:
            return False
        # 每个桶的和
        target = nums_sum / k
        # 标记元素使用状态，避免重复
        used = [False for i in range(n)]

        def back_track(bucket_num, bucket_sum, start):
            # base case 桶数为0, 所有桶都装满了
            if bucket_num == 0:
                return True
            # 装满了当前桶，递归穷举下一个桶的选择 让下一个桶从 nums[0] 开始选数字
            if bucket_sum == target:
                return back_track(bucket_num - 1, 0, 0)

            # 从start开始向后查询是否有有效的nums[1]
            for i in range(start, len(nums)):
                # nums[i]已经被使用
                if used[i]:
                    continue
                # 装不下
                if nums[i] + bucket_sum > target:
                    continue
                # 做选择，将nums[i]装入
                used[i] = True
                bucket_sum += nums[i]
                # 递归到下一层
                res = back_track(bucket_num, bucket_sum, i + 1)
                if res:
                    return True
                # 撤销选择
                used[i] = False
                bucket_sum -= nums[i]

            # 穷举了所有数字，都无法达到目标
            return False

        return back_track(k, 0, 0)


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    result = Solution().canPartitionKSubsets(nums, k)
    print(result)
