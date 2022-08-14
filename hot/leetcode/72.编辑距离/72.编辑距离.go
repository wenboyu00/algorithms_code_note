package main

import "fmt"

func minDistance(word1 string, word2 string) int {
	m, n := len(word1), len(word2)
	// init db table
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	// base case
	for i := 0; i < m+1; i++ {
		dp[i][0] = i
	}
	for j := 0; j < n+1; j++ {
		dp[0][j] = j
	}
	// 状态转移
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			// 循环中下标减一，下标变成了从0开始到结束
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				min := dp[i-1][j-1] + 1
				delOp := dp[i-1][j] + 1
				insertOp := dp[i][j-1] + 1
				if min > delOp {
					min = delOp
				}
				if min > insertOp {
					min = insertOp
				}
				dp[i][j] = min
			}
		}
	}
	return dp[m][n]
}

func main() {
	word1 := "horse"
	word2 := "ros"
	result := minDistance(word1, word2)
	fmt.Println(result)
}
