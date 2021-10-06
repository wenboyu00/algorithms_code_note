from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异位词，相同字母，不同位置
        排序后位置也相同，用排序后字母做为map的key，原字母作为val
         - 哈希表：{排序后字符串：[原字符串]}
        再遍历哈希表的values()即可
        """
        sorted_strs = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in sorted_strs:
                sorted_strs[ss].append(s)
            else:
                sorted_strs[ss] = [s]

        result = []
        for val in sorted_strs.values():
            result.append(val)
        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
