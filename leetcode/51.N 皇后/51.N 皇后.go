package main

import (
	"fmt"
	"strings"
)

func solveNQueens(n int) [][]string {
	// 初始化结果集
	result := make([][]string, 0)
	// 初始化棋盘
	board := make([][]string, n)
	for i := range board {
		col := make([]string, n)
		for j := range col {
			col[j] = "."
		}
		board[i] = col
	}
	backTrack(&board, 0, &result)
	return result
}
func backTrack(board *[][]string, row int, result *[][]string) {
	if row == len(*board) {
		strList := make([]string, 0)
		for _, strs := range *board {
			str := strings.Join(strs, "")
			strList = append(strList, str)
		}
		*result = append(*result, strList)
		return
	}

	n := len((*board)[row])
	for col := 0; col < n; col++ {
		if !isValid(board, row, col) {
			continue
		}
		(*board)[row][col] = "Q"
		backTrack(board, row+1, result)
		(*board)[row][col] = "."
	}
}
func isValid(board *[][]string, row int, col int) bool {
	n := len(*board)
	for i := 0; i < n; i++ {
		if (*board)[i][col] == "Q" {
			return false
		}
	}
	for i, j := row-1, col+1; i > -1 && j < n; i, j = i-1, j+1 {
		if (*board)[i][j] == "Q" {
			return false
		}
	}
	for i, j := row-1, col-1; i > -1 && j > -1; i, j = i-1, j-1 {
		if (*board)[i][j] == "Q" {
			return false
		}
	}
	return true
}

func main() {
	result := solveNQueens(4)
	fmt.Println(result)
}
