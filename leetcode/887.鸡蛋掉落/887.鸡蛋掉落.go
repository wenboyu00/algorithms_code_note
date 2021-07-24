package main

import (
	"fmt"
	"math"
)

func superEggDrop(k int, n int) int {
	memo := make([][]int, k+1)
	for i := range memo {
		rows := make([]int, n+1)
		for j := 0; j < len(rows); j++ {
			rows[j] = math.MaxInt32
		}
		memo[i] = rows

	}
	return dp(k, n, memo)
}

func dp(k int, n int, memo [][]int) int {
	if k == 1 {
		return n
	}
	if n == 0 {
		return 0
	}
	if memo[k][n] != math.MaxInt32 {
		return memo[k][n]
	}

	result := math.MaxInt16
	low, high := 1, n
	for low <= high {
		mid := (low + high) / 2
		broken := dp(k-1, mid-1, memo)
		notBroken := dp(k, n-mid, memo)
		if broken > notBroken {
			high = mid - 1
			if result > broken+1 {
				result = broken + 1
			}
		} else {
			low = mid + 1
			if result > notBroken+1 {
				result = notBroken + 1
			}
		}
	}
	memo[k][n] = result
	return result
}

func main() {
	result := superEggDrop(7, 10000)
	fmt.Println(result)

}
