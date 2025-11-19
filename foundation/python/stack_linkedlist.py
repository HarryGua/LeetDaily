"""
基于单链表实现的栈：1. peek() 栈顶: 链表的头节点 ( )
                  2. push() 入栈：将元素插入链表头部
                  3. pop() 出栈: 删除链表头节点

"""
class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None

class stack_linkedlist:
    def __init__(self) -> None:
        """构造函数"""
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """获得当前栈的大小"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断当前栈是否为空"""
        return self._size == 0
    
    def peek(self) -> int:
        """访问栈顶元素"""
        # 检查栈是否为空
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val # type: ignore
    
    def push(self, val: int):
        """入栈（在栈顶插入元素，或者说链表的头节点）"""
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:  #返回被删除的元素
        """出栈（删除栈顶的元素，或者说链表的头节点）"""
        # 检查栈是否为空
        if self.is_empty():
            raise IndexError("栈为空")
        num = self.peek()
        self._peek = self._peek.next # type: ignore
        self._size -= 1
        return num
    
    def to_list(self) -> list[int]:
        """转化为列表用于打印"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
    
    """Driver Code"""
if __name__ == "__main__":
    # 初始化栈
    stack = stack_linkedlist()

    # 元素入栈
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print("栈 stack =", stack.to_list())

    # 访问栈顶元素
    peek = stack.peek()
    print("栈顶元素 peek =", peek)

    # 元素出栈
    pop = stack.pop()
    print("出栈元素 pop =", pop)
    print("出栈后 stack =", stack.to_list())

    # 获取栈的长度
    size = stack.size()
    print("栈的长度 size =", size)

    # 判断是否为空
    is_empty = stack.is_empty()
    print("栈是否为空 =", is_empty)