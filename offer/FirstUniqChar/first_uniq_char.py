# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 示例 1:
# 输入：s = "abaccdeff"
# 输出：'b'

# 示例 2:
# 输入：s = "" 
# 输出：' '

class Solution:
    def firstUniqChar(self, s):
        # 用字典统计字符出现次数
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        for value in dic:
            if dic[value] == 1:
                return value
        return " "


if __name__ == "__main__":
    obj = Solution()
    s = "abaccdeff"
    res = obj.firstUniqChar(s)
    print(res)