package main

func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])
	count := 0
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	var dfs func(i int, j int)
	dfs = func(i int, j int) {
		if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == '0' {
			return
		}
		if visited[i][j] {
			return
		}
		visited[i][j] = true
		dfs(i+1, j)
		dfs(i-1, j)
		dfs(i, j+1)
		dfs(i, j-1)
	}
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if grid[row][col] == '1' && visited[row][col] != true {
				dfs(row, col)
				count += 1
			}
		}
	}
	return count
}

func main() {
	grid := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'}}
	println(numIslands(grid))
}
