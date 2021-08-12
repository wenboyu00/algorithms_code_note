package main

import (
	"sort"
)

func removeCoveredIntervals(intervals [][]int) int {
	// 排序规则，左端从大到小，右端从小到大
	less := func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] >= intervals[j][1]
		}
		return intervals[i][0] <= intervals[j][0]
	}
	// 进行排序
	sort.Slice(intervals, less)
	// 初始化记录区间
	left := intervals[0][0]
	right := intervals[0][1]
	res := 0
	n := len(intervals)
	for i := 1; i < n; i++ {
		// 记录左端小于当前左，大于当前右，找到覆盖区，数量+1
		if left <= intervals[i][0] && right >= intervals[i][1] {
			res += 1
		}
		// 记录右端在当前左右之间，找到交叉区间，更新记录右端位置为当前右
		if right >= intervals[i][0] &&  right <= intervals[i][1] {
			right = intervals[i][1]
		}
		// 记录右端位置小于当前左端，更新记录区间左右为当前左右
		if right <= intervals[i][0]{
			left = intervals[i][0]
			right = intervals[i][1]
		}
	}
	// 长度-覆盖数量 = 剩余数目
	return n - res
}

func main() {
	intervals := [][]int{{1, 4}, {3, 6}, {2, 8}}
	result := removeCoveredIntervals(intervals)
	println(result)
}
