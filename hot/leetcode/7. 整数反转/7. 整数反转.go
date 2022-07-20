package hot

func reverse(x int) int {
        res := 0
        for x !=0 {
            digit := x % 10
            x /= 10
            res = res*10+digit
        }
        if res < math.MinInt32 || res > math.MaxInt32{
            return 0
        }
        return res
}