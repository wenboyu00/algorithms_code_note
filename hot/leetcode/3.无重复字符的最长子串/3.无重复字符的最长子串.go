package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	window := map[int32]int{}
	left := 0
	right := 0
	result := 0
	for right < len(s) {
		c := int32(s[right])
		right += 1
		window[c] += 1
		for window[c] > 1 {
			d := int32(s[left])
			left += 1
			window[d] -= 1
		}
		if result < right-left {
			result = right - left
		}
	}
	return result
}

func main() {
	s := "abcabcbb"
	result := lengthOfLongestSubstring(s)
	fmt.Println(result)
}
