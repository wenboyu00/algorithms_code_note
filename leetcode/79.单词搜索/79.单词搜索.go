package main

func exist(board [][]byte, word string) bool {
	//先找到和第一个字母相同的格子，然后回溯寻找剩下的
	m := len(board)
	n := len(board[0])
	wordLen := len(word)
	visited := make([][]bool, m)

	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	var backtrack func(row int, col int, idx int) bool
	backtrack = func(row int, col int, idx int) bool {
		// 结束条件：字符索引到字符串尾部
		if idx == wordLen {
			return true
		}
		if row < 0 || col < 0 || row >= m || col >= n {
			return false
		}
		if visited[row][col] {
			return false
		}
		if board[row][col] != word[idx] {
			return false
		}
		// 添加选择
		visited[row][col] = true
		// 从格子的上下左右寻找和下一个字符 是否相等的结果
		if backtrack(row+1, col, idx+1) ||
			backtrack(row-1, col, idx+1) ||
			backtrack(row, col+1, idx+1) ||
			backtrack(row, col-1, idx+1) {
			return true
		}
		// 删除选择
		visited[row][col] = false
		return false
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if word[0] == board[i][j] {
				if backtrack(i, j, 0) {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	board := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
	word := "ABCCED"
	println(exist(board, word))
}
