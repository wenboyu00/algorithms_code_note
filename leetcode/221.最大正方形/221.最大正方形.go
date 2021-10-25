package main

func maximalSquare(matrix [][]byte) int {
	maxSide := 0
	m := len(matrix)
	n := len(matrix[0])
	if m == 0 || n == 0 {
		return maxSide
	}
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '1' {
				if i == 0 || j == 0 {
					dp[i][j] = 1
				} else {
					dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]) + 1
				}
				if maxSide < dp[i][j] {
					maxSide = dp[i][j]
				}
			}
		}
	}
	return maxSide * maxSide
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
