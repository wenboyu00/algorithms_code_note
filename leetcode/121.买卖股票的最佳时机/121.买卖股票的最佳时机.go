package main

import "math"

func maxProfit(prices []int) int {
	n := len(prices)
	dpi0 := 0
	dpi1 := math.MinInt32
	for i := 0; i < n; i++ {
		dpi0 = max(dpi0, dpi1+prices[i])
		dpi1 = max(dpi1, -prices[i])
	}
	return dpi0
}
func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}
func main() {
	p := []int{7, 1, 5, 3, 6, 4}
	result := maxProfit(p)
	print(result)
}
