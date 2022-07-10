package hot

import "strconv"

func findNthDigit(n int) int {
	start := 1
	digits := 1
	for n > 9*start*digits {
		n -= 9 * start * digits
		start *= 10
		digits += 1
	}
	num := start + (n-1)/digits
	index := (n - 1) % digits
	numStr := strconv.Itoa(num)
	return int(numStr[index] - '0')
}
