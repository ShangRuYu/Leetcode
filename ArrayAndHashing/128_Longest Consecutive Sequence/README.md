## 128. Longest Consecutive Sequence
[LeetCode Link](https://leetcode.com/problems/longest-consecutive-sequence/)
#### Description
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the array contain duplicates? Yes
2. Can the array be empty? Yes
3. Can numbers be negative? Yes
4. EDGE CASE:
   - Input: nums = [1,3,5,7,9], Output: 1 (each element is its own sequence)
   - Input: nums = [1,2,3,4,5], Output: 5
   - Input: nums = [1,2,3,10,11,12,13], Output: 4 (sequence [10,11,12,13])
   - Input: nums = [9,1,4,7,3,2,8,5,6], Output: 9 (entire array forms [1-9])

### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Hashset:<br>
Convert array into set for O(1) look up time. We can track the current number within the set to see wether the number is the start of the consecutive number, and the number that is larger exactly by 1 is exist in the set.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

1. First, convert the number array to set, for O(1) lookup time and avoid duplicate
2. Iterate through the set, check does the `current number - 1` exist in set, if exist then the current number is not the start of consecutive number, iterate to the next number
3. Check does the current number increase by 1 exist in the set, if exist, increase the length by 1, and compare with the max length when the while loop end
4. Return the max length

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
- Creating set from array: O(n)
- Iterating through set: O(n) iterations
- For each number:
  - Checking if num-1 exists: O(1)
  - If it's a start: counting sequence takes O(k) where k is sequence length
  


Space Complexity: O(n)
- Hash set stores all unique elements: O(n)
- A few variables (max_length, current_num, etc.): O(1)
- Total: O(n)