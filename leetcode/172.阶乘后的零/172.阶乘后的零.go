package main

func trailingZeroes(n int) int {
	res := 0
	divs := 5
	for divs <= n {
		res += n / divs
		divs *= 5
	}
	return res
}
