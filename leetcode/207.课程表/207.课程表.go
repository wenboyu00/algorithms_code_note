package main

func canFinish(numCourses int, prerequisites [][]int) bool {
	edges := make([][]int, numCourses)
	flags := make([]int, numCourses)
	for _, nums := range prerequisites {
		edges[nums[1]] = append(edges[nums[1]], nums[0])
	}

	var dfs func(idx int) bool
	dfs = func(idx int) bool {
		if flags[idx] == -1 {
			return true
		}
		if flags[idx] == 1 {
			return false
		}
		flags[idx] = 1
		for _, j := range edges[idx] {
			if dfs(j) == false {
				return false
			}
		}
		flags[idx] = -1
		return true
	}

	for i := 0; i < numCourses; i++ {
		if dfs(i) == false {
			return false
		}
	}
	return true
}

func main() {
	numCourses := 2
	prerequisites := [][]int{{1, 0}}
	println(canFinish(numCourses, prerequisites))
}
