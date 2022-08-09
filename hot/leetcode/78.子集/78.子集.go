package main

import "fmt"

func subsets(nums []int) [][]int {
	n := len(nums)
	// 路径列表
	track := make([]int, 0, n)
	res := [][]int{}

	var backTrack func(start int)
	backTrack = func(start int) {
		// 把路径添加到结果集，生成新的数组的方式
		res = append(res, append(make([]int, 0, n), track...))
		// 遍历选择
		for i := start; i < n; i++ {
			// 做选择
			track = append(track, nums[i])
			// 递归
			backTrack(i + 1)
			// 取消选择
			track = track[:len(track)-1]
		}
	}
	backTrack(0)
	return res
}

func main() {
	nums := []int{1, 2, 3}
	result := subsets(nums)
	fmt.Println(result)
}
