# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# example
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reverseList(self, head):
        res = None
        while head:
            value = ListNode(head.val) # 1 2 
            value.next = res # ->NULL => 1->NULL  2 -> 1->NULL
            res = value # 1->NULL => 2 -> 1->NULL 
            head = head.next 
        return res

if __name__ == "__main__":
    head = ListNode([1,2,3,4,5])
    obj = Solution()
    print(obj.reverseList(head).val)

        
