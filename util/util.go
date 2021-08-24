package util

func IntMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
func Intmax(a int, b int) int {
	if a < b {
		return b
	} else {
		return a
	}
}

func IntPow(n, m int) int {
	if m == 0 {
		return 1
	}
	result := n
	for i := 2; i <= m; i++ {
		result *= n
	}
	return result
}
