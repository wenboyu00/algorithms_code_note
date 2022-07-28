package hot
func longestCommonPrefix(strs []string) string {
    for i:=0; i<len(strs[0]);i++{
        c := strs[0][i]
        for j:=1; j < len(strs);j++{
            if i == len(strs[j]) || c != strs[j][i]{
                return strs[0][:i]
            }
        }
    }
	return strs[0]
}