package main

import "math"

/*
对比122，增加了手续费。
把手续费从卖出时减去即可
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
*/
func maxProfit(prices []int, fee int) int {
	n := len(prices)
	dpi0 := 0
	dpi1 := math.MinInt32
	for i := 0; i < n; i++ {
		temp := dpi0
		dpi0 = max(dpi0, dpi1+prices[i]-fee)
		dpi1 = max(dpi1, temp-prices[i])
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
	p := []int{1, 3, 2, 8, 4, 9}
	f := 2
	result := maxProfit(p, f)
	print(result)
}
