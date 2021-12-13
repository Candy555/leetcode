# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        # 从上到下打印，层次遍历，广度优先搜索（BFS） => 队列，先入先出
        if not root:
            return []

        res = []
        # collections 中的双端队列 deque()， popleft() 方法可达到 O(1)时间复杂度
        queue = collections.deque()
        queue.append(root)
        # print(queue.append(root.val))
        while queue:
            tmp = []
            # [3, 9, 20, None, None, 15, 7]
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

        for idx in range(len(res)):
            if idx%2 != 0:
                res[idx].reverse()
        return res


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode([3,9,20,None,None,15,7])
    res = obj.levelOrder(root)
    print(res)