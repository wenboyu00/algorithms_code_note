package main

import "strings"

func letterCombinations(digits string) []string {
	phone := map[byte][]string{
		'2': {"a", "b", "c"},
		'3': {"d", "e", "f"},
		'4': {"g", "h", "i"},
		'5': {"j", "k", "l"},
		'6': {"m", "n", "o"},
		'7': {"p", "q", "r", "s"},
		'8': {"t", "u", "v"},
		'9': {"w", "x", "y", "z"}}
	path := []string{}
	result := []string{}
	n := len(digits)
	if n == 0 {
		return result
	}
	var backtrack func(path []string, index int)
	backtrack = func(path []string, index int) {
		// 满足结束条件
		if len(path) == n {
			result = append(result, strings.Join(path, ""))
			return
		}
		// 循环选择
		digit := digits[index]
		for _, s := range phone[digit] {
			// 做选择
			path = append(path, s)
			backtrack(path, index+1)
			path = path[:len(path)-1]
		}
	}
	backtrack(path, 0)
	return result
}
