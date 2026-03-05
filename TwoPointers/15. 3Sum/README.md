## 15. 3Sum
[LeetCode Link](https://leetcode.com/problems/3sum/description/)
#### Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the array contain duplicates? Yes
2. How should we handle duplicate triplets in the result? Avoid returning duplicate triplets
3. Can numbers be negative? Yes
4. EDGE CASE:
   - Input: nums = [0,1,1], Output: []
   - Input: nums = [0,0,0], Output: [[0,0,0]]
   - Input: nums = [-1,-1,-1,0,1,2], Output: [[-1,0,1],[-1,-1,2]]

### Match
> - See if this problem matches a problem category and strategies or patterns within the category

HashMap:<br>
Use a hash map that stores how many times each number appears.
As we pick the first and second numbers, we temporarily reduce their counts in the map so we don't reuse them. Then we check whether the needed third value still exists in the map.
Sorting also helps us skip duplicates easily so we only add unique triplets. Time: O(n^2), Space:O(n).

Two Pointer:<br>
After sorting the array, we can fix one number and then search for the other two using the two-pointer technique.
Sorting helps us skip duplicates easily and moving the left or right pointer will increase or decrease the sum in a predictable way.
For each fixed number a, we place two pointers:
left starts just after i,right starts at the end.
If the current sum is too large, we move r left to reduce it.
If the sum is too small, we move l right to increase it.
When the sum is exactly zero, we record the triplet and skip duplicates. Time: O(n), Space:O(1).

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram
Start traversing inwards, from both ends of the input string, and we can expect to see the same characters, in the same order

1) Sort the input array
2) Initialize two pointers, `left` and `right`, where `left` starts from `i + 1`, and `right` starts from the end of the array. Here, `i` represents the current index of the element `n`
3) Check if the sum of the numbers pointed to by these two pointers is equal to 0
    - If it is equal, add them to the triplets array
        - Skip if the next `num[left]` is equal to the previous one by increment `left` by 1
        - Skip if the next `num[right]` is equal to the previous one by decrement `right` by 1
    - If it is too large, decrement the right pointer by 1
    - Otherwise, increment the left pointer by 1 since it is too small
4) Return ans


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

Time Complexity: O(n^2)
1. Sorting: O(n log n)

2. Outer loop: O(n)
   - Iterates through n elements
   
3. Inner two-pointer search: O(n) for each iteration
   - For each fixed element, pointers traverse remaining array
   - left and right pointers together make at most n moves
   
4. Total: O(n log n) + O(n) * O(n) = O(n log n) + O(n²)


Space Complexity: O(1) or O(n)
- If using in-place sort (like heapsort): O(1) extra space
- If using merge sort or timsort (Python default): O(n) space
- Result array doesn't count toward space complexity