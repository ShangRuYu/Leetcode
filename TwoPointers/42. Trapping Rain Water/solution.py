class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3: # If the input list is empty or has less than 3 elements, return 0
            return 0

        left, right = 0, len(height) - 1
        # Initialize the maximum height from the left and right
        maxLeft, maxRight = height[left], height[right]
        result = 0

        while left < right: # Loop until the two pointers meet
            if maxLeft < maxRight: # If the maximum height on the left is less than the maximum height on the right
                left += 1
                maxLeft = max(height[left], maxLeft) # Update the maximum height from the left
                result += maxLeft - height[left] # Calculate the trapped water at the current position and add it to the result
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                result += maxRight - height[right]
        return result