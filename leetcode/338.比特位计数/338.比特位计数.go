package main

func countBits(n int) []int {
	// dp数组，结果数组，存放十进制数对应的二进制1的个数
	// base case：result[0] = 1 ，0的二进制1的个数是0
	// 状态转移方程：
	//	当i为奇数时1的个数 = i-1 +1，因为奇数比上一个数（偶数）多1，这个1出现在低位上。
	//	当i为偶数时1的个数 = i/2，因为i/2相当于去掉一个0，偶数低位是0。
	result := make([]int, n+1)
	for i := 1; i < n+1; i++ {
		if i%2 == 1 {
			result[i] = result[i-1] + 1
		} else {
			result[i] = result[i/2]
		}
	}
	return result
}
