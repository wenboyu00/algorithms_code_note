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
		var res = make([]int, 0, i+1)
		for j := 0; j < i+1; j++ {
			if j == 0 || j == i {
				res = append(res, 1)
			} else {
				pre := result[i-1]
				num := pre[j] + pre[j-1]
				res = append(res, num)
			}
		}
		result = append(result, res)
	}
	return result
}

func main() {
	result := generate(5)
	fmt.Println(result)
}
