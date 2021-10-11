package main

func uniquePaths(m int, n int) int {
	dp := make([][]int, m)
	// base case
	// 第一列 只有向下一种走法,初始化为 1
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		dp[i][0] = 1
	}
	// 第一行 只有向右一种走法,初始化为 1
	for j := 0; j < n; j++ {
		dp[0][j] = 1
	}
	// 动态转移方程
	// 达到i,j的路径数 = i-1,j(上一个格子) + i,j-1(左一个格子)
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}
	return dp[m-1][n-1]
}

func main() {
	println(uniquePaths(3, 7))
}
