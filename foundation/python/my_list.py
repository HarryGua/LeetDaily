# 动态数组 / 简易版列表 的实现
"""
重点设计：
1. 初始容量：选取一个合理的 数组初始容量。
2. 数量记录：声明一个变量 size 用于记录列表当前元素数量；根据此变量可以定位到列表尾部，以及判断是否需要扩容
3. 扩容机制: 当数组元素个数增加至底层静态数组容量的上限时，扩容为原来的2倍；
                        /缩减至底层静态数组容量的1/4时，缩容为原来的1/2
"""

class my_list:
    """列表实现"""

    def __init__(self) -> None:
        """构造方法"""
        self._capacity: int = 10    # 列表容量
        self._arr: list[int] = [0] * self._capacity # 数组（存储列表元素） 
        self._size: int = 0 # 列表长度（当前元素数量）

    def size(self) -> int:
        """获取列表长度（当前列表容量）"""
        return self._size
    
    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity
    
    def get(self, index: int) -> int:
        """访问元素"""
        # 索引如果越界，则抛出异常
        if index < 0 or index >= self._size:
            raise IndexError("索引越界") 
        return self._arr[index]
    
    def set(self, num: int, index: int) -> None:
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def _resize(self, new_capacity):
        """将列表的 size 改为新的 size"""
        self._capacity = new_capacity
        temp = [0] * new_capacity
        for i in range(self._size):
            temp[i] = self._arr[i]
        self._arr = temp

    # 增：
    def add(self, num: int):
        """在尾部增加元素"""
        # 边界检查，如果 size 数据量 达到了列表的capacity容量，则扩容
        if self.size() == self.capacity():
            self._resize(2 * self._capacity)
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """在中间插入元素"""
        # 索引越界检查
        if index < 0 or index > self._size:  #允许尾部插入
            raise IndexError("索引越界")

        # 边界检查，如果存储的数据量 size 达到了列表的容量 capacity，则扩容
        if self.size() == self.capacity():
            self._resize(2 * self._capacity)

        # 将索引index以及之后的元素都向后移动一位（从后向前遍历避免覆盖）
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        self._size += 1

    # 删
    def remove(self, index: int) -> int:
        """删除元素"""
        # 索引检查
        if index < 0 or index > self._size:     
            raise IndexError("索引越界")
        
        # 可以缩容节约空间
        if self._size <= self._capacity // 4 and self._capacity > 10:  # 保持最小容量
            self._resize(self._capacity // 2)
        
        removed_num = self._arr[index]
        # 将索引index之后的元素都向前移动一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # 更新元素数量
        self._size -= 1
        # 返回被删除的元素
        return removed_num
    
    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]
# usage example
if __name__ == "__main__":
    # 初始化列表
    nums = my_list()
    # 在尾部添加元素
    nums.add(1)
    nums.add(3)
    nums.add(2)
    nums.add(5)
    nums.add(4)
    
    print(nums.to_array())

    # 在中间插入元素
    nums.insert(6, index=3)

    print(nums.to_array())

    # 删除元素
    nums.remove(3)
    print(nums.to_array())
    # 访问元素
    num = nums.get(1)
    print(nums.to_array())
    # 更新元素
    nums.set(0, 1)
    print(nums.to_array())
    # 测试扩容机制
    for i in range(20):
        nums.add(i)
    print(nums.to_array())
    # 测试缩容机制:
    for i in range(15):
        nums.remove(0)
    print(nums.to_array())