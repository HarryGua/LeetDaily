# 1. iteration

def for_loop(n: int) -> int:
    """1. for loop"""
    res = 0
    # 循环求和 1+2+3+...+n, 求和结果用res记录
    for i in range(1, n + 1):
        res += i

    return res

def while_loop(n: int) ->int:
    """"2. while loop"""
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

def nested_for_loop(n: int) -> str:
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j})"
    return res


# recursion 
"""
递归：通过函数调用自身来解决问题，主要包含两个阶段：
1. 递：程序不断调用自身，传入更小/更简化的参数，直到达到“终止条件”。
2. 归：触发“终止条件”后，程序从最深层的递归函数开始逐层返回，汇聚每一层的结果

递归的3个实现的要素：
1. 终止条件：决定什么时候由“递”转“归”
2. 递归调用：对应“递”，函数调用自身；
3. 返回结果：对应“归”，将当前递归层级的结果返回至上一层。
"""

def recur(n: int) -> int:
    """递归"""
    # 终止条件
    if n == 1:
        return 1
    # 递：递归调用
    res = recur(n -1)
    # 归：返回结果
    return n + res

def tail_recur(n, res):
    """尾递归"""
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)
"""
普通递归：求和操作是在“归”的过程中执行的；
尾递归：求和操作是在“递”的过程中执行的
"""

"""
设斐波那契数列0，1，1，2，3，5，8，13，...., 求该数列的第n个数字
"""

def fib(n: int) -> int:
    """递归树/斐波那契数列：递归"""
    # 终止条件 f(1) = 0, f(2) = 1
    if n == 1 or n == 2:
        return n - 1
    # 递归调用f(n) = f(n-1) + f(n-2)
    res = fib(n - 1) + fib(n - 2)
    return res

if __name__ == "__main__":
    print(nested_for_loop(6))