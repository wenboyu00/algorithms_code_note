package main

func minPathSum(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	// base case
	// 初始化dp结构
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	// 初始化dp数值
	dp[0][0] = grid[0][0]
	// 第一列，每个格子值 = 上个格子+当前
	for i := 1; i < m; i++ {
		dp[i][0] = dp[i-1][0] + grid[i][0]
	}
	// 第一行，每个格子 = 左个格子+当前
	for j := 1; j < n; j++ {
		dp[0][j] = dp[0][j-1] + grid[0][j]
	}
	// 状态转移
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			// 当前格子和 = 上一个格子和左一个格子中取最小的路径和+当前格子值
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}
	return dp[m-1][n-1]
}

func min(int1 int, int2 int) int {
	if int1 > int2 {
		return int2
	} else {
		return int1
	}
}

func main() {
	grid := [][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}
	println(minPathSum(grid))
}
