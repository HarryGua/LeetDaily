class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        双指针解法：
        第一个指针循环数组中的所有数字，嵌套第二个指针循环其余数字
        相加与目标值进行比较: if 相等时输出答案; else 继续进行比较
        """
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return []