package main

import "fmt"

func combine(n int, k int) [][]int {
	track := make([]int, 0, k)
	res := [][]int{}
	var backTrack func(start int)
	backTrack = func(start int) {
		//  满足结束条件,到达树底
		if len(track) == k {
			res = append(res, append(make([]int, 0, 2), track...))
			return
		}
		for i := start; i < n+1; i++ {
			// 做选择
			track = append(track, i)
			// dfs
			backTrack(i + 1)
			// 撤销选择
			track = track[:len(track)-1]
		}
	}
	backTrack(1)
	return res
}

func main() {
	n := 4
	k := 2
	result := combine(n, k)
	fmt.Println(result)
}
