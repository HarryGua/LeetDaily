class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        容积 = (height[left] 和 height[right]中更小的哪一个) * (right - left)
        largest volume
        """
        left = 0
        right = len(height) - 1
        largest_vol = 0

        while left < right:
            volume = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            largest_vol = max(volume, largest_vol)
        return largest_vol