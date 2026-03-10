class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the area formed by the lines at the left and right pointers
            # Height is the minimum of the two heights
            amount = (right - left) * min(height[left], height[right])
            result = max(result, amount)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result