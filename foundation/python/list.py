# 初始化列表
# 无初始值
nums1: list[int] = []
# 有初始值
nums2: list[int] = [1, 3, 2, 5, 4]

# 访问元素
num: int = nums2[1] 
# 更新元素
nums2[1] = 0

# 插入与删除元素
# 清空列表
nums1.clear()

# 在中间插入元素
nums1.insert(3, 6) # 在索引3处插入数字6

# 删除元素
nums1.pop(3)

# 4. 遍历列表
# 通过索引遍历列表
count = 0
for i in range(len(nums2)):
    count += nums2[i]

# 直接遍历列表元素
for num in nums2:
    count += num

# 5. 拼接两个列表
# 给定一个新列表 nums1, 我们可以将其拼接到原列表的尾部
nums1: list[int] = [6, 8, 7, 10, 9]
nums2 += nums1 #将列表nums1拼接在nums2之后

# 排序列表
nums1.sort() #排序后，列表元素从小到大排列