## 238. Product of Array Except Self
[LeetCode Link](https://leetcode.com/problems/product-of-array-except-self/description/)
#### Description
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Will the input contains negative and zero? Yes
2. Can it run in O(n) time? Yes
3. EDGE CASE:
   - Input: nums = [-1,0,1,2,3], Output: [0,-6,0,0,0]
   - Input: nums = [-3,3], Output: [3,-3]



### Match
> - See if this problem matches a problem category and strategies or patterns within the category

1. Left and Right product lists / Pointers <br>
We can create two lists: one to store the product of all numbers to the left of each element and another to store the product of all numbers to the right of each element. By multiplying the corresponding elements from these two lists, we can compute the desired result.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

1. Create a empty array to store the product result
2. Go through two iterations from left to right and right to left, and collect the product of each iteration
   - In the first pass, we fill `res[i]` with the product of all elements to the left of i
   - In the second pass, we multiply each `res[i]` with the product of all elements to the right of i
3. Create a variable leftProduct = 1, since no product before index 0
4. Set `res[i] = leftProduct` (product of all elements to the left). Update `leftProduct *= nums[i]`
5. Create a `rightProduct = 1` and do the second pass. For each index i, multiply `res[i]` by rightProduct. Update `rightProduct *= nums[i]`
6. Return the result array

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Time Complexity: O(n)
- Build prefix array: O(n)
- Build suffix array: O(n)
- Combine results: O(n)
- Total: O(3n) = O(n)

Space Complexity: O(n)
- Prefix array: O(n)
- Suffix array: O(n)
- Total: O(n) 