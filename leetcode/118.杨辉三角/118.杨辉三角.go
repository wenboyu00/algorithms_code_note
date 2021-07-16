package main

import "fmt"

/*
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
*/
func generate(numRows int) [][]int {
	// 创建[][]空切片, len=0, cap=numRows
	result := make([][]int, 0, numRows)
	for i := 0; i < numRows; i++ {
		// 创建[]空切片, len=0, cap=i+1
		res := make([]int, i+1)
		// 列表前后的值都设为1
		res[0] = 1
		res[i] = 1
		// 遍历把中间的值 = 左上角（result[i-1][j]）+ 右上角 result[i-1][j-1]
		for j := 1; j < i; j++ {
			res[j] = result[i-1][j] + result[i-1][j-1]
		}
		result = append(result, res)
	}
	return result
}

func main() {
	result := generate(5)
	fmt.Println(result)
}
