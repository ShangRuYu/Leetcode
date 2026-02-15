## 49. Group Anagrams
[LeetCode Link](https://leetcode.com/problems/top-k-frequent-elements/description/)
#### Description
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the array contain negative numbers or zeros?
    - Yes
2. Can the array be empty?
    - No
3. What if all elements have the same frequency?
    - Return all k elements
4. EDGE CASE:
    - Input: nums = [1,1,1,1], k = 1, Output: [1]
    - Input: nums = [1,2,3], k = 3, Output: [1,2,3]

### Match
> - See if this problem matches a problem category and strategies or patterns within the category
1. Sort and HashMap, O(nlogn):
   - Create a HashMap to store the frequent and value. Secondly, create a list of`[frequency, number]` from the map, sort the list and repeatedly pop from the end of the sorted list add to the result list, stop while reach k elements in the result list
2. Min-Heap, O(nlogk):
   - Create frequency map that counts how many times each number appears. Create a min-heap and push each number `(frequency, number)` to the map, if the size of map larger than k, pop once. Pop all the number from the min-heap and store the number into result list.
3. Bucket Sort, O(n):
   - Use a hash map to count the frequency of each element. Create an array of "buckets," where each bucket corresponds to a specific frequency count. Place elements into their respective buckets based on their frequencies. Start from the highest-frequency bucket and collect elements until you have k elements.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

Bucket Sort:
1. Build a frequency map that counts how many times each number appears.
2. Create a list of groups `freq`, where `freq[i]` will store all numbers that appear exactly i times.
3. For each number and its frequency in the map, add the number to `freq[frequency]`.
4. Initialize an empty result list.
5. Loop from the largest possible frequency down to 1:
    - For each number in `freq[i]`, add it to the result list.
    - Once the result contains k numbers, return it.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

- n = length of input array
- m = number of unique elements

MinHeap approach:
- Time Complexity: O(n log k)
   - Counting frequencies: O(n)
   - Building heap: 
     - For each unique element (m elements)
     - Push to heap: O(log k)
     - Total: O(m log k)
   - Since m ≤ n, overall: O(n + m log k) = O(n log k) when k is small
   - Extracting k elements: O(k log k)
   - Total: O(n log k)

- Space Complexity: O(n)
  - Frequency map: O(m) where m ≤ n
  - Heap: O(k)
  - Result: O(k)
  - Total: O(n)

Sorting:
- Time Complexity: O(n log n)
  - Counting frequencies: O(n)
  - Sorting m elements: O(m log m)
  - Since m ≤ n, total: O(n log n)

- Space Complexity: O(n)
  - Frequency map: O(m)
  - Sorted list: O(m)
  - Total: O(n)

Bucket Sort:
- Time Complexity: O(n)
  - Counting frequencies: O(n)
  - Building buckets: O(m) where m ≤ n
  - Collecting results: O(n) worst case iterate all buckets
  - Total: O(n)

- Space Complexity: O(n)
  - Frequency map: O(m)
  - Buckets array: O(n) (size = len(nums) + 1)
  - Result: O(k)
  - Total: O(n)
