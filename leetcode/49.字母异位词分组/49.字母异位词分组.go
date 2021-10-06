package main

import "sort"

func groupAnagrams(strs []string) [][]string {
	mapping := map[string][]string{}
	for _, str := range strs {
		// 转换成字节数组，并进行排序
		s := []byte(str)
		sort.Slice(s, func(i, j int) bool {
			return s[i] < s[j]
		})
		sortedStr := string(s)
		mapping[sortedStr] = append(mapping[sortedStr], str)
	}
	result := make([][]string, 0, len(mapping))
	for _, val := range mapping {
		result = append(result, val)
	}
	return result
}
