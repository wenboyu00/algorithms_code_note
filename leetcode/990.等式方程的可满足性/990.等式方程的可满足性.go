package main

func equationsPossible(equations []string) bool {
	// 初始化并查集合数组
	parent := make([]int, 26)
	for i := 0; i < 26; i++ {
		parent[i] = i
	}
	// 相等，连通
	for _, str := range equations {
		if str[1] == '=' {
			// -'a' 后范围是0~25 刚好和parent数组长度一致，节省空间
			index1 := int(str[0] - 'a')
			index2 := int(str[3] - 'a')
			union(parent, index1, index2)
		}
	}
	// 不相等，判断根节点是否一致，一致表示已经相等过，等式不成立 False
	for _, str := range equations {
		if str[1] == '!' {
			index1 := int(str[0] - 'a')
			index2 := int(str[3] - 'a')
			if find(parent, index1) == find(parent, index2) {
				return false
			}
		}
	}
	return true
}

func union(parent []int, index1, index2 int) {
	parent[find(parent, index1)] = find(parent, index2)
}
func find(parent []int, index int) int {
	for parent[index] != index {
		parent[index] = parent[parent[index]]
		index = parent[index]
	}
	return parent[index]
}

func main() {
	str := []string{"c==c","b==d","x!=z"}
	result := equationsPossible(str)
	println(result)
}