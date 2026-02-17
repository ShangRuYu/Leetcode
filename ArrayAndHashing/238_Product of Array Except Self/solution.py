class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left_product = 1 # Calculate the product of all elements to the left of the current index
        for i in range(len(nums)):
            result[i] = left_product # Store the left product in the result array
            left_product *= nums[i] # Update the left product for the next iteration

        right_product = 1
        for i in range(len(nums)-1, -1, -1): # Calculate the product of all elements to the right of the current index
            result[i] *= right_product
            right_product *= nums[i]

        return result
    
# nums:    1    2    3    4
# left:    1    1    2    6
# right:   24   12   4    1
# result:  24   12   8    6