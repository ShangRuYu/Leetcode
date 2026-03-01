class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Convert to set for O(1) lookup. This also removes duplicates
        longest = 0

        for num in numSet:
            if num - 1 not in numSet: # Only start counting from the beginning of a sequence
                curNum = num          # If num-1 exists, then num is not the start
                length = 1

                while curNum + 1 in numSet: # Count consecutive numbers
                    curNum += 1
                    length += 1
            
                longest = max(longest, length)
        return longest