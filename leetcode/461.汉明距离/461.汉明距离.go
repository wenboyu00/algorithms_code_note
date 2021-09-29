package main

func hammingDistance(x int, y int) int {
	// 异或运算，得出两数不同位置上的1，
	n := x ^ y
	count := 0
	for n != 0 {
		// n&(n-1)去掉最后一位的1，对1进行计数
		n = n & (n - 1)
		count += 1
	}
	return count
}
