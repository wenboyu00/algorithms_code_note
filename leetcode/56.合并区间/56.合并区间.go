package main

import (
	"fmt"
	"sort"
)

func merge(intervals [][]int) [][]int {
	less := func(i, j int) bool {
		return intervals[i][0] <= intervals[j][0]
	}
	// 进行排序
	sort.Slice(intervals, less)
	res := [][]int{intervals[0]}
	for i := 1; i < len(intervals); i++ {
		cur := intervals[i]
		last := res[len(res)-1]
		if cur[0] <= last[1] {
			last[1] = max(cur[1], last[1])
		} else {
			res = append(res, cur)
		}
	}
	return res
}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	intervals := [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}
	result := merge(intervals)
	fmt.Println(result)
}
