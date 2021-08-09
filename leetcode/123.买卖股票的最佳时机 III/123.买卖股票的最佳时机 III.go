package main

import "math"

func maxProfit(prices []int) int {
	n := len(prices)
	dp := make([][][]int32, 0)
	for i := 0; i < n; i++ {
		kk := make([]int32, 0)
		for k := 0; k < 3; k++ {
			kk = append(kk, []int32{0, math.MinInt32}...)
		}
		dp[i] = kk
	}
}

func main() {
	p := []int{3, 3, 5, 0, 0, 3, 1, 4}
	result := maxProfit(p)
	print(result)
}
