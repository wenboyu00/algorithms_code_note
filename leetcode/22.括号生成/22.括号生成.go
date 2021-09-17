package main

import (
	"fmt"
	"strings"
)

func generateParenthesis(n int) []string {
	res := []string{}
	if n == 0 {
		return res
	}
	track := []string{}
	var backtrack func(left int, right int)
	backtrack = func(left int, right int) {
		if left > right {
			return
		}
		if left < 0 || right < 0 {
			return
		}
		if left == 0 && right == 0 {
			res = append(res, strings.Join(track, ""))
			return
		}
		track = append(track, "(")
		backtrack(left-1, right)
		track = track[:len(track)-1]

		track = append(track, ")")
		backtrack(left, right-1)
		track = track[:len(track)-1]
	}
	backtrack(n, n)
	return res
}

func main() {
	n := 3
	result := generateParenthesis(n)
	fmt.Println(result)
}
