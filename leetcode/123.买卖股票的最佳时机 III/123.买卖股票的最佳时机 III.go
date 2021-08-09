package main

func maxProfit(prices []int) int {
	n := len(prices)
	// 初始化 dp数组，用base case作为默认值
	dp := make([][][]int, 0)
	for i := 0; i < n; i++ {
		kk := make([][]int, 0)
		for k := 0; k < 3; k++ {
			kk = append(kk, []int{0, -prices[i]})
		}
		dp = append(dp, kk)
	}
	for i := 0; i < n; i++ {
		for k := 2; k > 0; k-- {
			if i == 0 {
				continue
			}
			dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
			dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

		}

	}
	return dp[n-1][2][0]
}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	p := []int{3, 3, 5, 0, 0, 3, 1, 4}
	result := maxProfit(p)
	print(result)
}
