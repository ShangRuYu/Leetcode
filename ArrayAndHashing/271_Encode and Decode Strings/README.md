## 271. Encode and Decode Strings 
[LeetCode Link](https://leetcode.com/problems/encode-and-decode-strings/description/)
#### Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.


Machine 1 (sender) has the function:<br>
```
        string encode(vector<string> strs) {
        // ... your code
        return encoded_string;
        }
```

Machine 2 (receiver) has the function:<br>
```
        vector<string> decode(string s) {
        //... your code
        return strs;
        }
```

Machine 1 does:<br>
`string encoded_string = encode(strs);`<br>

Machine 2 does:<br>
`vector<string> strs2 = decode(encoded_string)`;<br>
strs2 in Machine 2 should be the same as strs in Machine 1.<br>


Implement the encode and decode methods.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string contain any character? Yes
2. Can the strng be empty? Yes
3. EDGE CASE:
   - Input: ["", ""], Decoded: ["", ""]
   - Input: ["hello#world", "test:data"], Decoded: ["hello#world", "test:data"]

### Match
> - See if this problem matches a problem category and strategies or patterns within the category
1. String Manipulation:
   This is a serialization/deserialization problem, the problem involves handling strings in various ways, such as replacing characters, splitting strings, and building new strings based on specific rules. Simple delimiters like `,` or `#` won't work if strings contain them. Solution: Use length + delimiter format: `length#string`

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

We use `length#string` to store the string. `#` can be the boundary between string and string's length, to help us locate where should the decode process start
1. Create a empty string to store `length#string`
2. Iterate through the input string and count the length of the stirng, append `length#string` format into the create string
3. Create a empty list to store the decoded result, two pointers to locate the string and delimiter
4. While `i` in bound
   - move `j` forward until it finds `#`
   - Convert the substring `s[i:j]` into an integer length, since the number before `#` is the length of string
   - Move `i` to the character right after `#`
   - Append the extracted string to the result list
   - Move `i` forward by length to continue decoding the next segment.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


- n = number of strings in the list
- k = average length of strings
- m = total number of characters across all strings (m = n * k)

Time Complexity: O(m) where m = total characters
- Iterate through n strings: O(n)
- For each string, append length + "#" + string: O(k)
- String concatenation in Python can be O(m) due to immutability
- Total: O(n * k) = O(m)

Space Complexity: O(m)
- Encoded string contains all original characters plus delimiters
- Length digits: O(n) worst case
- Delimiters: O(n)
- Original content: O(m)
- Total: O(m)