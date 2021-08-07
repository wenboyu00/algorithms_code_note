package main

import "fmt"

func findAnagrams(s string, p string) []int {
	need := map[int32]int{}
	window := map[int32]int{}
	for _, i := range p{
		need[i] += 1
		window[i] = 0
	}
	left := 0
	right := 0
	valid := 0
	var result []int
	for right < len(s) {
		c := int32(s[right])
		right += 1
		if _, ok := need[c]; ok {
			window[c] += 1
			if window[c] == need[c] {
				valid += 1
			}
		}
		for right-left >= len(p) {
			if valid == len(need) {
				result = append(result, left)
			}
			d := int32(s[left])
			left += 1
			if _, ok := need[d]; ok {
				if window[d] == need[d] {
					valid -= 1
				}
				window[d] -= 1
			}
		}
	}
	return result
}
func main() {
	s := "cbaebabacd"
	p := "abc"
	result := findAnagrams(s, p)
	fmt.Println(result)
}
