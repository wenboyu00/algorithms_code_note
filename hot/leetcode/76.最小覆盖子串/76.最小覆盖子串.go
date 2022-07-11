package main

import (
	"fmt"
)

func minWindow(s string, t string) string {
	//range遍历的字符串是int32格式
	need := map[int32]int{}
	window := map[int32]int{}
	for _, v := range t {
		need[v] += 1
		window[v] = 0
	}
	left := 0
	right := 0
	start := 0
	valid := 0
	strLen := len(s) + 1
	for right < len(s) {
		// 扩大窗口，找到可行解
		// 和int32格式map的key 统一格式
		c := int32(s[right])
		right += 1
		if _, ok := need[c]; ok {
			window[c] += 1
			// 增加有效字符
			if window[c] == need[c] {
				valid += 1
			}
		}
		// 减小窗口，优化可行解
		for valid == len(need) {
			// 新的结果结果比旧的结果短，再更新
			if right-left < strLen {
				start = left
				strLen = right - left
			}
			d := int32(s[left])
			left += 1
			if _, ok := need[d]; ok {
				// 减少有效字符
				if window[d] == need[d] {
					valid -= 1
				}
				window[d] -= 1
			}

		}
	}
	if strLen == len(s)+1 {
		return ""
	}
	//和python使用一样
	return s[start : start+strLen]
}

func main() {
	s := "ADOBECODEBANC"
	t := "ABC"
	result := minWindow(s, t)
	fmt.Println(result)
}
