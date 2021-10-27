package main

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := 1; i < n+1; i++ {
		dp[i] = i
		for j := 1; i-j*j >= 0; j++ {
			num := i - j*j
			if dp[i] > dp[num]+1 {
				dp[i] = dp[num] + 1
			}
		}
	}
	return dp[n]
}
func main() {
	println(numSquares(12))
}
