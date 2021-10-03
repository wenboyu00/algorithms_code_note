from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        组合-回溯
            - 可重复组合+多数求和
        可重复组合->用回溯算法
            - 避免重复->设置当前递归起始位置
        求和，逐次减值方式，=0时 就满足条件，<0 就超过条件
        剪枝，在进入递归之前发现 减去当前值<0 直接返回
        """
        result = []
        path = []

        def backtrack(target, start):
            # 满足条件
            if target == 0:
                result.append(list(path))
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 剪枝，<0 不满足需要
                if target - num < 0:
                    return
                # 加入选择
                path.append(num)
                # 递归，减去当前值为目标值和从当前起点向后搜索
                backtrack(target - num, i)
                # 撤销选择
                path.pop()

        candidates = sorted(candidates)
        backtrack(target, 0)
        return result


if __name__ == '__main__':
    # candidates = [2, 3, 6, 7]
    # target = 7
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
