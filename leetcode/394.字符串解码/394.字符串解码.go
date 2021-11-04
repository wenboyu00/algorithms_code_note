package main

import (
	"fmt"
	"strconv"
	"strings"
)

func decodeString(s string) string {
	// 存储重复倍数的栈和储存之前的栈
	numStack := []int{}
	strStack := []string{}
	num := 0
	ans := ""
	for _, c := range s {
		if c >= '0' && c <= '9' {
			n, _ := strconv.Atoi(string(c))
			num = num*10 + n
		} else if c == '[' {
			numStack = append(numStack, num)
			strStack = append(strStack, ans)
			num = 0
			ans = ""
		} else if c == ']' {
			curNum := numStack[len(numStack)-1]
			numStack = numStack[:len(numStack)-1]
			lastAns := strStack[len(strStack)-1]
			strStack = strStack[:len(strStack)-1]
			ans = lastAns + strings.Repeat(ans, curNum)
		} else {
			ans += string(c)
		}
	}
	return ans
}

func main() {
	s := "3[a2[c]]"
	fmt.Println(decodeString(s))
}
