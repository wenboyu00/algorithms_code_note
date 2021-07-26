package main

import "fmt"

func permute(nums []int) [][]int {
	var result [][]int
	// 选择列表
	var track []int
	// 辅助判断是否使用
	used := make([]bool, len(nums))
	backTrack(nums, track, &result, &used)
	return result
}

func backTrack(nums []int, track []int, result *[][]int, used *[]bool) {
	// 满足结束条件,达到叶子根节点，将路径装入结果列表
	if len(nums) == len(track) {
		trackTemp := make([]int, len(track))
		copy(trackTemp, track)
		*result = append(*result, trackTemp)
		return
	}
	for i, v := range nums {
		// 判断是否使用
		if !(*used)[i] {
			// 做选择，路径.append(路径)
			track = append(track, v)
			(*used)[i] = true
			// 进入下一层决策树
			backTrack(nums, track, result, used)
			// 撤销选择，将该选择再次加入列表
			track = track[:len(track)-1]
			(*used)[i] = false
		}
	}
}
func main() {
	nums := []int{1, 2, 3}
	result := permute(nums)
	fmt.Println(result)
}
