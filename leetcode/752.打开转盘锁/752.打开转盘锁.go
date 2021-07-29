package main

import (
	"fmt"
	"strconv"
	"strings"
)

func openLock(deadends []string, target string) int {
	//初始化切片作为队列
	q := []string{}
	//初始化已访问集合用于去重
	visited := make(map[string]string)
	q = append(q, "0000")
	visited[q[0]] = q[0]
	// 初始化死亡数字集合用于实现快速查询
	deadendsSet := make(map[string]string)
	for _, v := range deadends {
		deadendsSet[v] = v
	}

	step := 0

	for len(q) != 0 {
		size := len(q)
		// 讲当前队列总的节点向四周扩散
		for i := 0; i < size; i++ {
			cur := q[0]
			q = q[1:]
			// 判断是否到终点
			if cur == target {
				return step
			}
			// 跳过无效数字集合
			if _, ok := deadendsSet[cur]; ok {
				continue
			}
			// 把相邻的节点加入队列
			for j := 0; j < 4; j++ {
				up := plusOne(cur, j)
				if _, ok := visited[up]; !ok {
					q = append(q, up)
					visited[up] = up
				}
				down := minusOne(cur, j)
				if _, ok := visited[down]; !ok {
					q = append(q, down)
					visited[down] = down
				}
			}
		}
		step += 1
	}
	return -1
}

func plusOne(s string, i int) string {
	//分割为字符串数组
	ch := strings.Split(s, "")
	if ch[i] == "9" {
		ch[i] = "0"
	} else {
		// 先转换为数字，然后+1再转回str
		num, _ := strconv.Atoi(ch[i])
		ch[i] = strconv.Itoa(num + 1)
	}
	//拼接回字符串
	return strings.Join(ch, "")
}

func minusOne(s string, i int) string {
	ch := strings.Split(s, "")
	if ch[i] == "0" {
		ch[i] = "9"
	} else {
		num, _ := strconv.Atoi(ch[i])
		ch[i] = strconv.Itoa(num - 1)
	}
	return strings.Join(ch, "")
}

func main() {
	deadends := []string{"0201", "0101", "0102", "1212", "2002"}
	target := "0202"
	result := openLock(deadends, target)
	fmt.Println(result)
	//res := plusOne("2021", 1)
	//fmt.Println(res)

}
