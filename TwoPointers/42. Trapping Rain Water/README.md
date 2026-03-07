## 42. Trapping Rain Water
[LeetCode Link](https://leetcode.com/problems/trapping-rain-water/description/)
#### Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. What's the minimum length of the array? Can be any length, but 0, 1, 2 can't trap water
2. EDGE CASE:
   - Input: height = [5], Output: 0 (need at least 2 bars to trap water)
   - Input: height = [], Output: 0


### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Two Pointer:<br>
Water at position i is determined by:
1. Highest bar to the left of i
2. Highest bar to the right of i
3. Water level = min(left_max, right_max) - height[i]

If water level ≤ 0, no water trapped at that position. Time: O(n), Space:O(1).

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

We don't need to know both max_left and max_right for ALL positions.
We only need to know which side is smaller.

If left_max < right_max:
  - Water at left position is limited by left_max
  - We can calculate water at left position
  - Move left pointer

If right_max < left_max:
  - Water at right position is limited by right_max
  - We can calculate water at right position
  - Move right pointer

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
- Single pass through array: O(n)
   - Each element processed exactly once

Space Complexity: O(1)
 - Only use constant variables
   - left, right, left_max, right_max, water: O(1)