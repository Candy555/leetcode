# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

#  

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:return 0
        lookup = []
        cur_len, max_len = 0, 0
        str_len = len(s)
        for i in range(str_len):
            val = s[i]
            if val not in lookup:
                lookup.append(val)
                cur_len += 1

            else:
                index = lookup.index(val)
                lookup = lookup[index+1:]
                lookup.append(val)
                cur_len = len(lookup)
            if cur_len > max_len:
                max_len = cur_len
        return max_len

