"""
使用数组实现栈时: 1. peek() 栈顶：将数组的尾部作为栈顶
                 2. pop() 出栈：在数组的尾部删除元素
                 3. push() 入栈：在数组的尾部增加元素
"""


class stack_array:
    def __init__(self) -> None:
        """构造函数"""
        self._stack: list[int] = []
    
    def size(self) -> int:
        """获取栈的长度"""
        return len(self._stack)
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self.size() == 0
    
    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    
    def pop(self) -> int:
        """出栈（在数组的尾部删除元素）"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()
    
    def push(self, num: int):
        """入栈（在数组的尾部插入元素）"""
        self._stack.append(num)

    def to_list(self) -> list[int]:
        """作为列表返回"""
        return self._stack
    
"""Driver Code"""
if __name__ == "__main__":
    # 初始化栈
    stack = stack_array()

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