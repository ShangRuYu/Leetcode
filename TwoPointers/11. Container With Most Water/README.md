## 11. Container With Most Water
[LeetCode Link](https://leetcode.com/problems/container-with-most-water/)
#### Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can heights be zero or negative? Yes, but no negative
2. What's the minimum length of the array? 2 to form a container
3. What's amount of container? Area = min(height[i], height[j]) × (j - i)
4. EDGE CASE:
   - Input: height = [1,100,1], Output: 2 (indices 0 and 2: min(1,1) × 2 = 2)
   - Input: height = [4,4,4,4], Output: 12 (indices 0 and 3: min(4,4) × 3 = 12)


### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Two Pointer:<br>
1. Start with widest container (left=0, right=n-1)
2. Greedy strategy: Move the pointer with smaller height inward
3. Moving the taller pointer cannot improve the result
4. Track maximum area found

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

1. Create a result to store the max area of water
2. Initiate left at 0, right pointer at the end of array
   - Use while loop `left < right`
   - Calculate current pointer's amount of water
   - Update the result to track max area
3. Iterate through the array by moving the pointer
   - Left <= Right, move left. Else move right
4. Return result

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
- Each pointer moves at most n times
- Left pointer: moves from 0 to at most n-1
- Right pointer: moves from n-1 to at most 0
- Total pointer movements: at most n
- Each iteration: O(1) operations (min, multiply, compare)
- Total: O(n)

Space Complexity: O(1)
- Two pointer variables (left, right): O(1)
- Max area variable: O(1)
- Temporary variables for calculations: O(1)