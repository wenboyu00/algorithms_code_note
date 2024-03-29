package main

import (
	"algorithms-code-note/util"
	"fmt"
)

func coinChange(coins []int, amount int) int {
	memo := make([]int, amount+1)

	for i := range memo {
		memo[i] = -666
	}
	return dp(coins, amount, memo)
}
func dp(coins []int, amount int, memo []int) int {
	if amount == 0 {
		return 0
	}
	if amount < 0 {
		return -1
	}
	if memo[amount] != -666 {
		return memo[amount]
	}
	maxValue := len(memo) + 1
	res := maxValue
	for _, coin := range coins {
		subProblem := dp(coins, amount-coin, memo)
		if subProblem == -1 {
			continue
		}
		// 分解子问题 + 一枚
		res = util.IntMin(res, subProblem+1)
	}
	memo[amount] = res
	if res == maxValue {
		memo[amount] = -1
	}
	return memo[amount]

}

func main() {
	result := coinChange([]int{1, 2, 5}, 11)
	fmt.Println(result)
}
