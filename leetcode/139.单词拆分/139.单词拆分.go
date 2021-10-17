package main

func wordBreak(s string, wordDict []string) bool {
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for low := 0; low < n; low++ {
		if !dp[low] {
			continue
		}
		for _, word := range wordDict {
			high := low + len(word)
			if high < n+1 && s[low:high] == word{
				dp[high] = true
			}
		}

	}
	return dp[n]
}
