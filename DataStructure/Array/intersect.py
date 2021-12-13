# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]

# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]


import collections


class Solution:
    def intersect(self, nums1, nums2):
        # 由于同一个数字在两个数组中都可能出现多次，因此需要用哈希表存储每个数字出现的次数。
        # 对于一个数字，其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        # 首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，
        for num in nums1:
            m[num] += 1

        # 然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
        intersection = list()
        for num in nums2:
            if (m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        return intersection


if __name__ == "__main__":
    obj = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = obj.intersect(nums1, nums2)
    print(res)
