## 167. Two Sum II Input Array Is Sorted
[LeetCode Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
#### Description
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the array contain duplicates? Yes
2. Can we use the same number twice? No
3. Can numbers be negative? Yes
4. EDGE CASE:
   - Input: numbers = [-1,0,3,5], target = 2, Output: [1,3]  # -1 + 3 = 2
   - Input: numbers = [1,2,2,3], target = 4, Output: [1,4]  # 1 + 3 = 4

### Match
> - See if this problem matches a problem category and strategies or patterns within the category

HashMap:<br>
Store each number in the array to map, map store `{number: index}`. Iterate through the array and calculate `target - numbers[i]` to get the corresponding number. If the complement number is in the map then return the result. If no pair is found, return an empty list. Time: O(n), Space:O(n).

Two Pointer:<br>
One start at the left, another start at the end of array. If the sum of pointers are insufficient, move the left pointer to the next index. When the sum is too high, move the right pointer. Repeat the process until find the result. Time: O(n), Space:O(1).

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

1. First, initiate two pointer, one point to the start of array, one point to the end of array
2. Create a while loop, when right pointer > left pointer, get the sum of two pointer and compare with target value.
3. If the sum larger than target, move the right pointer left. If sum is  lesser, move left pointer right.
4. Return the index of two number if exist, otherwise return empty list

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

n = length of input array

Time Complexity: O(n)
- Initialize pointers: O(1)
- While loop: At most n iterations
  - In each iteration, we move at least one pointer
  - Left pointer moves right at most n times
  - Right pointer moves left at most n times
  - Total pointer movements: at most n
  - Each iteration does O(1) work (comparison, addition)
- Total: O(n)

Space Complexity: O(1)
- Two pointer variables (left, right): O(1)
- One variable for sum: O(1)
- Return array of size 2: O(1)
- Total: O(1) constant extra space