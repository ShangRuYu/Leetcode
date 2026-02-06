## 49. Group Anagrams
[LeetCode Link](https://neetcode.io/problems/anagram-groups/question)
#### Description
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Will the string contains only one word or empty string? What should return?
   - YES, the return Ans will be `[[""]] ` in this case.
2. Will there be no anagram case?
   - Based on constraints (1 ≤ strs.length), the array will have at least one string.
3. HAPRRY PATH:
   - Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
   - Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
4. EDGE CASE: 
   - Input: [""], Output: [[""]]
   - Input: ["a"], Output: [["a"]]

### Match
> - See if this problem matches a problem category and strategies or patterns within the category
1. Sort:
   - Sort the string so we will get the character in order. If two strings are anagrams, two sorted string will be the same. Sorting will cost O(nlogn) time.
2. HashMap:
   - Create a hash map and the key is the sorted string, and the value is a list of strings belonging to that anagram group. `"sorted string": [list of strings having the same key]`.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

Sort and Map approach:
1. Create a HashMap
2. Iterate through the string
   - Sort the string 
   - Append the sorted string to the corresponding list, if the key doesn't exist, creaete a new key-value pair
3. Return the value of the map 

String character frequency approach:
 - Every string is lowercase English letters, use a array size of 26 can store each string's letter frequencies, anagrams will have the same frequency.
1. Create a HashMap
2. Iterate through the string, and create a array size of 26, this will be the key of HashMap
3. Use `ord` to mark each character in the string, increment the count at the corresponding index
4. Trun the array into tuple and store as a key, and append the string into HashMap correspondly
5. Return the value of map as list


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

For the Sort and Map approach:
  - Time complexity: O(n * k log k) 
    - n = number of strings in the array
    - k = maximum length of a string
    - For each string: sorting takes O(k log k)
    - We do this n times: n * k log k
 - Space complexity: O(n * k)
   - HashMap stores n strings, each up to length k
   - Sorted keys also take O(n * k) space
  
For String character frequency approach:
- Time Complexity: O(n * k)
  - n = number of strings
  - k = maximum length of a string
  - For each string: counting characters takes O(k)
  - Creating the tuple key takes O(26) = O(1)
  - Total: n * k = O(n * k)
  
- Space Complexity: O(n * k)
  - HashMap stores n strings: O(n * k)
  - Count arrays: each is size 26, for n strings = O(26n) = O(n)
  - Total: O(n * k)