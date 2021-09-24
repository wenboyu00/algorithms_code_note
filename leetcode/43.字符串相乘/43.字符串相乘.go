package main

import (
	"strconv"
)

func multiply(num1 string, num2 string) string {
	if num1 == "0" && num2 == "0" {
		return "0"
	}
	m, n := len(num1), len(num2)
	res := make([]int, m+n)
	for i := m - 1; i >= 0; i-- {
		n1 := int(num1[i] - '0')
		for j := n - 1; j >= 0; j-- {
			n2 := int(num2[j] - '0')
			sum := res[i+j+1] + n1*n2
			res[i+j+1] = sum % 10
			res[i+j] += sum / 10
		}
	}
	ans := ""
	index := 0
	if res[0] == 0 {
		index = 1
	}
	for ; index < m+n; index++ {
		ans += strconv.Itoa(res[index])
	}
	return ans
}

func main() {
	num1 := "123"
	num2 := "456"
	result := multiply(num1, num2)
	println(result)
}
