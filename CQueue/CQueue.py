# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

# example1
# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]] 
# 输出：[null,null,3,-1]

# example2:
# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]

"""
#题解 
["CQueue","appendTail","deleteHead","deleteHead"] 表示每一次操作的集合数组
[[],[],[5],[2],[],[]] 这个表示每一次操作后对应的参数的集合数组
1、CQueue
首先初始化，没有参数，所以是 []，然后我们注意到 CQueue() 函数是没有返回值的，用 null 来表示（不要问我为什么用 null 表示。。。）
2、deleteHead
删除操作，没有参数，所以是 []，根据题意若队列中没有元素，deleteHead 操作返回 -1 ，所以输出值为 -1 。
3、appendTail
插入操作，有参数，此时是 **5 **，并且 appendTail() 函数没有返回值的，用 null 来表示。
4、appendTail
插入操作，有参数，此时是 **2 **，并且 appendTail() 函数没有返回值的，用 null 来表示。
5、deleteHead
删除操作，没有参数，所以是 []，此时队列中有元素，先进入的是 5，后进入的是 2，根据队列 先进先出 的性质，元素 5 出列，所以返回值是 5 。
6、deleteHead
删除操作，没有参数，所以是 []，此时队列中有元素，只有元素 2，所以返回值是 2 。
"""


class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        #如果是栈的插入操作，那可以把元素都先插入到 stack1 中，也就实现了队列的 入队操作 。
        self.stack1.append(value)
    
    def deleteHead(self):
        """
        当 stack2 中不为空时，直接操作，此时在 stack2 中的栈顶元素是最先进入队列的元素，返回该元素即可；
        如果 stack2 为空且 stack1 也为空，返回 -1；
        如果 stack2 为空且 stack1 不为空，首先需要把 stack1 中的元素逐个弹出并压入到 stack2 中，然后返回 stack2 的栈顶元素即可。
        """
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()

if __name__ == "__main__":
    obj = CQueue()
    value = [[],[],[5],[2],[],[]]
    obj.appendTail(value)
    param_2 = obj.deleteHead()
    print(param_2)
            
            
