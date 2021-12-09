# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

class Solution:
    def replaceSpace(self, s):
        if not s: 
            return ""
        str1 = ""
        for character in s:
            if character == " ":
                str1 += "%20"
            else:
                str1 += character
        return str1

if __name__ == "__main__":
    obj = Solution()
    s = "We are happy."
    result = obj.replaceSpace(s)
    print(result)
