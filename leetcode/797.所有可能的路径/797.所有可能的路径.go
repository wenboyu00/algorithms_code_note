package main

func allPathsSourceTarget(graph [][]int) [][]int {
	// 回溯算法，DFS
	res := [][]int{}
	// 储存路径
	path := []int{}

	var traverse func(graph [][]int, s int, path []int)
	traverse = func(graph [][]int, s int, path []int) {
		// 记录路径
		path = append(path, s)
		// base case 到达终点，保存
		if s == len(graph)-1 {
			// 把路径添加到结果集中,从路径中移除节点s
			res = append(res, append([]int{}, path...))
			path = path[:len(path)-1]
			return
		}
		// 递归每个相邻的节点
		for _, v := range graph[s] {
			traverse(graph, v, path)
		}
		// 从路径移除节点 s
		path = path[:len(path)-1]
	}
	traverse(graph,0,path)
	return res
}
