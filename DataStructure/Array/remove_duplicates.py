# version_1
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 为什么返回数值是整数，但输出的答案是数组呢?
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

# example1
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

# example2
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        i = 0
        for idx in range(1, len(nums)):
            if nums[i] != nums[idx]:
                i += 1
                nums[i] = nums[idx]
        return i+1


#version_2
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

#  

# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#  

# 示例 1：
# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
# 示例 2：
# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3]
# 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
class Solution2:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == "__main__":
    obj = Solution2()
    nums = [3,2,2,3]
    val = 3
    length = obj.removeElement(nums, val)
    print(length)



            





