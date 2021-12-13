# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：

# [3,9,20,15,7]


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        # 从上到下打印，按层打印，广度优先搜索（BFS） => 队列，先入先出
        if not root:
            return []

        res = []
        # collections 中的双端队列 deque()， popleft() 方法可达到 O(1)时间复杂度
        queue = collections.deque()
        queue.append(root)
        # print(queue.append(root.val))
        while queue:
            # [3, 9, 20, None, None, 15, 7]
            # node = TreeNode(queue.popleft())
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode([3,9,20,None,None,15,7])
    res = obj.levelOrder(root)
    print(res)
