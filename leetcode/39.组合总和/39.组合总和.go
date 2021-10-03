package main

import "sort"

func combinationSum(candidates []int, target int) [][]int {
	// 回溯算法-组合，用startIndex来控制重复选择
	result := [][]int{}
	path := []int{}
	n := len(candidates)
	var backtrack func(target int, start int)
	backtrack = func(target int, start int) {
		// 满足条件
		if target == 0 {
			result = append(result, append([]int{}, path...))
			return
		}
		// 遍历选择
		for i := start; i < n; i++ {
			num := candidates[i]
			// 剪枝，超出范围
			if target-num < 0 {
				return
			}
			// 添加选择
			path = append(path, num)
			// 回溯（减去当前值=目标值，起始位置为当前位置->去掉重复)
			backtrack(target-num, i)
			// 撤销选择
			path = path[:len(path)-1]
		}
	}
	// 排序
	sort.Ints(candidates)
	backtrack(target, 0)
	return result
}
