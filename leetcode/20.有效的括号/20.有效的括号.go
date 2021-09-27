package main

func isValid(s string) bool {
	if len(s)%2 == 1 {
		return false
	}
	mapping := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}
	stk := []rune{}
	for _, ch := range s {
		if val, ok := mapping[ch]; ok {
			if len(stk) == 0 || stk[len(stk)-1] != val{
				return false
			}
			stk = stk[:len(stk)-1]
		} else {
			stk = append(stk, ch)
		}
	}
	return len(stk) == 0
}
func main() {
	s := "()[]{}"
	println(isValid(s))
}
