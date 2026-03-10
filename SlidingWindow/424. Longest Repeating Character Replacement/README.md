## 424. Longest Repeating Character Replacement
[LeetCode Link](https://leetcode.com/problems/longest-repeating-character-replacement/description/)
#### Description
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can k be 0 or larger than string size? Yes
2. What if the string is empty? Return 0
3. EDGE CASE:
   - Input: s = "ABABAB", k = 2, Output: 5 (e.g., "AABAB" → "AAAAA")
   - Input: s = "AABBA", k = 0, Output: 2 (substring "AA" or "BB")

### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Sliding Window:<br>
1. Need to find the longest valid window where replacements ≤ k
2. Key Formula: window_size - max_frequency ≤ k
    - window_size = total characters in window
    - max_frequency = count of most frequent character in window
    - window_size - max_frequency = characters that need replacement
3. Use frequency map to track character counts in window

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

1. Create a map to store character frequency in current window
2. Create a mostSeenChar to track frequency and a result to store longest char
3. Initiate left at 0, right pointer interate through the string
   - add right pointer character `s[right]` into map and update frequency
   - update the mostSeenChar to maintain the highest frequent
4. If the window is invalid `window size - maxf > k`, shrink the left pointer
5. Update the result with the valid window size.
6. Return result

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
- Right pointer traverses string once: O(n)
- Left pointer moves at most n times total
- Each character added once to frequency map: O(n)
- Each character removed at most once: O(n)
- Frequency map operations (get, set): O(1)
- max_freq update: O(1)
- Total: O(n)

Space Complexity: O(1)
- Frequency map: at most 26 entries (uppercase letters A-Z)
- Variables (left, right, max_freq, max_length): O(1)
- Total: O(26) = O(1)