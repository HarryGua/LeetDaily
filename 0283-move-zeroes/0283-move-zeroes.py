class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        双指针解法：
        1. 左右指针开局指向同一位置
        2. 左指针指向已排序的尾部，右指针指向待处理数组的头部
        3. 右指针不断向右移动，每次右指针指向非零数，则做右指针对应的数交换，同时左指针右移
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
            right += 1