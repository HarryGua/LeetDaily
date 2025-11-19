"""
  方法         描述             时间复杂度
push()  元素入栈（添加至栈顶）      O(1)
pop()       栈顶元素出栈           O(1)
peek()      访问栈顶元素           O(1)
"""
# 初始化栈
# Python 没有内置的栈类，可以把list当作栈来使用
stack: list[int] = [ ]

# 元素入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

print("stack = ", stack)

# 访问栈顶元素
peek: int = stack[-1]
print("栈顶元素 peek = ", peek)

# 元素出栈
pop: int = stack.pop()
print("出栈元素 pop = ", pop)

# 获取栈的长度
size: int = len(stack)
print("栈的长度 size = ", size)

# 判断是否为空
is_empty:bool = len(stack) == 0