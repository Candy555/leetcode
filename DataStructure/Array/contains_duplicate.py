# 给定一个整数数组，判断是否存在重复元素。
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# example1:
# 输入: [1,2,3,1]
# 输出: true

# example2:
# 输入: [1,2,3,4]
# 输出: false

# example3:
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true


class Solution:
    def contains_duplicate(self, nums):
        if not nums:
            return 0
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4]
    result = obj.contains_duplicate(nums)
    print(result)
