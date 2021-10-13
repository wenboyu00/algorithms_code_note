package main

func exist(board [][]byte, word string) bool {
	m := len(board)
	n := len(board[0])
	wordLen := len(word)
	visited := make([][]bool, m)

	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	var backtrack func(row int, col int, idx int) bool
	backtrack = func(row int, col int, idx int) bool {
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
		visited[row][col] = true
		if backtrack(row+1, col, idx+1) ||
			backtrack(row-1, col, idx+1) ||
			backtrack(row, col+1, idx+1) ||
			backtrack(row, col-1, idx+1) {
			return true
		}

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
