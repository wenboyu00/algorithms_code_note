package main

func searchMatrix(matrix [][]int, target int) bool {
	/*
	直觉法，利用单调性
	行列数据都是单调递增
	y轴x轴 相等于2个指针，根据数据的单调性移动指针
	从右上角出发，matrix[y][x]
	大于target，就减小x指针
	小于target，就增大y指针
	注意：指针越界
	*/
	m := len(matrix)
	n := len(matrix[0])
	x := n-1
	y := 0
	for x >= 0 && y < m {
		if matrix[y][x] > target {
			x -= 1
		} else if matrix[y][x] < target {
			y += 1
		} else {
			return true
		}
	}
	return false
}

func main() {
	matrix := [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}
	target := 5
	println(searchMatrix(matrix, target))

}
