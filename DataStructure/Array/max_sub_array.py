# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。

# example1:
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

# example2:
# 输入：nums = [1]
# 输出：1

# example3:
# 输入：nums = [5,4,-1,7,8]
# 输出：23

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        maxSum, tempSum = nums[0], nums[0]
        for num in nums[1:]:
            tempSum = max(num, num + tempSum)
            maxSum = max(tempSum, maxSum)
        return maxSum

if __name__ == "__main__":
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maxSum = obj.maxSubArray(nums)
    print(maxSum)