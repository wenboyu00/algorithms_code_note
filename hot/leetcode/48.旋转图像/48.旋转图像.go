package main

func rotate(matrix [][]int) {
	n := len(matrix)
	// 对角线 翻转
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			tmp := matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = tmp
		}
	}
	// 垂直 翻转
	for i := 0; i < n; i++ {
		for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
			tmp := matrix[i][left]
			matrix[i][left] = matrix[i][right]
			matrix[i][right] = tmp
		}
	}
}
