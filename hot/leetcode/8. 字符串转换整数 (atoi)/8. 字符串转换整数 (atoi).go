package main

import "math"

func myAtoi(s string) int {
	res := 0
	sign := 1
	start := 0
	// 去掉前段空格
	n := len(s)
	for start < n && s[start] == ' ' {
		start += 1
	}
	if start == n {
		return 0
	}

	// 存储正负号
	if s[start] == '-' {
		sign = -1
		start += 1
	} else if s[start] == '+' {
		start += 1
	}
	// 把字符串转换为数字
	for start < n && s[start] >= '0' && s[start] <= '9' {
		res = res*10 + sign*int(s[start]-'0')
		start += 1
        // 溢出判断
		if res > math.MaxInt32 {
			return math.MaxInt32
		}
		if res < math.MinInt32 {
			return math.MinInt32
		}
	}

	return res
}

func main() {
	s := "9223372036854775808"
	println(myAtoi(s))
}
