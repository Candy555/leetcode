# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3

#  

# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
     def isSymmetric(self, root):
         if not root: return True
         def Symmetric(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and Symmetric(node1.left, node2.right) and Symmetric(node1.right, node2.left)
            else:
                return node1 is node2
         return Symmetric(root.left, root.right)
         