package main

func maxProfit(k int, prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}
	if k > n/2 {
		k = n / 2
	}
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		kList := make([][]int, k+1)
		for j := 0; j < k+1; j++ {
			kList[j] = []int{0, -prices[i]}
		}
		dp[i] = kList
	}
	for i := 0; i < n; i++ {
		for j := k; j > 0; j-- {
			if i == 0 {
				continue
			}
			dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
			dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
		}
	}
	return dp[n-1][k][0]
}

func max(int1 int, int2 int) int {
	if int1 < int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	k := 2
	prices := []int{2, 4, 1}
	result := maxProfit(k, prices)
	println(result)
}
