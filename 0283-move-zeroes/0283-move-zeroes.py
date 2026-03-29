class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        双指针解法：
        1. 左右指针开局指向同一位置
        2. 左指针指向已排序的尾部，右指针指向待处理数组的头部
        3. 右指针不断向右移动，每次右指针指向非零数，则做右指针对应的数交换，同时左指针右移
        """
        left = right = 0
        for right in range(left, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
