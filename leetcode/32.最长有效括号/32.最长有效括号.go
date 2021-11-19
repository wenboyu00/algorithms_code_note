package main

func longestValidParentheses(s string) int {
	/*
	栈
	- 用无法匹配的右括号索引做分割，存入栈底，base case: -1作为初始化的无法匹配的索引
	- 入栈的(的索引和后面)的索引匹配，弹出(索引后，右括号索引和栈底元素索引之间的差值就是有效括号的长度。
	*/
	maxAns := 0
	stk := []int{-1}
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stk = append(stk, i)
		} else {
			stk = stk[:len(stk)-1]
			if len(stk) == 0 {
				stk = append(stk, i)
			} else {
				sLen := i - stk[len(stk)-1]
				if sLen > maxAns {
					maxAns = sLen
				}
			}
		}
	}
	return maxAns
}

func main() {
	print(longestValidParentheses("(()"))
}
