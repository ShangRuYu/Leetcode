class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # Sort the array in order to avoid duplicates and use two pointers
        result = []
        
        # We stop at len(nums) - 2 because we need at least 3 numbers to make a triplet
        for i in range(len(nums) - 2): 
            # Skip duplicate values for the first number in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
             
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the second and third numbers in the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return result