package main

func calculate(s string) int {
	stk := []int{}
	sign := '+'
	num := 0
	for i, ch := range s {
		isDigit := '0' <= ch && ch <= '9'
		if isDigit {
			num = 10*num + int(ch-'0')
		}
		if !isDigit && ch != ' ' || i == len(s)-1 {
			if sign == '+' {
				stk = append(stk, num)
			} else if sign == '-' {
				stk = append(stk, -num)
			} else if sign == '*' {
				stk[len(stk)-1] *= num
			} else if sign == '/' {
				stk[len(stk)-1] /= num
			}
			num = 0
			sign = ch
		}
	}
	ans := 0
	for _, v := range stk {
		ans += v
	}
	return ans
}

func main() {
	s := "3+2*2"
	result := calculate(s)
	println(result)
}
