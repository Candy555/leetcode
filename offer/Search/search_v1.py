# 统计一个数字在排序数组中出现的次数。

# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0

# 二分查找
class Solution:
    def Search(self, nums, target):
        # 搜索右边界 right
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j -= 1
        right = i
        # 搜索左边界 left
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j -= 1
        left = j
        return right - left - 1 


if __name__ == "__main__":
    obj = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    result = obj.Search(nums, target)
    print(result)

