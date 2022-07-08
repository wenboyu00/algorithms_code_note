package main

func permutation(s string) []string {
	track := make([]byte, 0, len(s))
	result := map[string]bool{}
	visit := make([]bool, len(s), len(s))
	for i := 0; i < len(s); i++ {
		visit[i] = false
	}
	var backTrack func()
	backTrack = func() {
		if len(track) == len(s){
			result[string(track)] = true
			return
		}
		for idx, _ := range s{
			if visit[idx] == true{
				continue
			}
			track = append(track, s[idx])
			visit[idx] = true
			backTrack()
			track = track[:len(track)-1]
			visit[idx] = false

		}
	}
	backTrack()
	res := make([]string, 0, len(result))
	for k := range result{
		res = append(res, k)
	}
	return res
}

func main() {
	s := "abc"
	println(permutation(s))
}