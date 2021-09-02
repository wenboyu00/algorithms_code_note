package main

import "fmt"

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	stack := []int{}
	res := make([]int, len(temperatures))
	for i := n - 1; i >= 0; i-- {
		for len(stack) != 0 && temperatures[i] >= temperatures[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) != 0 {
			res[i] = stack[len(stack)-1] - i
		}
		stack = append(stack, i)
	}
	return res
}

func main() {
	temperatures := []int{89, 62, 70, 58, 47, 47, 46, 76, 100, 70}
	result := dailyTemperatures(temperatures)
	fmt.Println(result)
}
