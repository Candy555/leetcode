# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

# 示例 1:
# 输入: [0,1,3]
# 输出: 2

# 示例 2:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8

class Solution:
    def missingNumber(self, nums):
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == mid:
                i = mid + 1
            else:
                j -= 1
        return i 


if __name__ == "__main__":
    obj = Solution()
    nums = [0,1,2,3,4,5,6,7,9]
    result = obj.missingNumber(nums)
    print(result)