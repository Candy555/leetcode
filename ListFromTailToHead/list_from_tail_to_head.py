# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# example
# 输入：head = [1,3,2]
# 输出：[2,3,1]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

if __name__ == "__main__":
    head = ListNode([1,3,2])
    test = Solution()
    print(test.reversePrint(head))

        
