# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 示例 1
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
# 示例 4:
# 输入: nums = [1,3,5,6], target = 0
# 输出: 0
# 示例 5:
# 输入: nums = [1], target = 0
# 输出: 0

class Solution:
    #二分查找
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    obj = Solution()
    nums = [1,3,5,6]
    target = 0
    result = obj.searchInsert(nums, target)
    print(result)
