## 3. Longest Substring Without Repeating Characters
[LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
#### Description
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty? Yes, return 0
2. EDGE CASE:
   - Input: s = "bbbbb", Output: 1 (substring is "b")
   - Input: s = "ab cd", Output: 4 (substring is "ab c" or "b cd")
   - Input: s = "abcda", Output: 4 (substring is "abcd" or "bcda")


### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Sliding Window:<br>
Need to track a window of unique characters, use Hash Map/Set to track characters in current window, expand window when unique, shrink when duplicate found, track maximum window size seen

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

Two pointers maintain a valid window:
   - Right pointer expands window (add elements)
   - Left pointer contracts window (remove elements)
   - Track optimal window throughout

Set approach:
   - When duplicate found, remove one by one from left
   - Requires while loop: while s[right] in set
   
   HashMap approach:
   - Stores last seen index
   - Can jump directly: left = last_index + 1
   - No while loop needed

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

n = length of string<br>
m = size of character set

Time Complexity: O(n)
1. Sliding Window with Set:
   - Right pointer traverses string once: O(n)
   - Left pointer moves at most n times total (not n per iteration!)
   - Each character added once, removed at most once
   - Total operations: O(2n) = O(n)

2. Sliding Window with HashMap:
   - Right pointer traverses string once: O(n)
   - Left pointer jumps directly, no while loop
   - Each character processed exactly once
   - HashMap operations (insert, lookup): O(1)
   - Total: O(n)

Space Complexity: O(min(n,m))
1. Sliding Window with Set:
   - Set stores at most min(n, m) characters
   - If string length < charset size: O(n)
   - If charset size < string length: O(m)
  
2. Sliding Window with HashMap:
   - HashMap stores at most min(n, m) entries