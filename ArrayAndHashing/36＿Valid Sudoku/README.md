## 36. Valid Sudoku
[LeetCode Link](https://leetcode.com/problems/valid-sudoku/)
#### Description
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

### Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Is the board always be 9x9? Yes.
2. What defines the 3x3 sub-boxes? The board is divided into 9 non-overlapping 3x3 boxes
3. EDGE CASE:
   - Input: [["5","3","5",...], ...], Output: false, duplicates in the same row
   - Input: [["5",...],["5",...], ...], Output: false, duplicates in the same column
   - Input: [["5","3","."],["6","5","."], ...]Output: false, duplicates in the same box
   
### Match
> - See if this problem matches a problem category and strategies or patterns within the category

Hashset:<br>
Iterate through rows, columns, and boxes, record numbers in the board. Use sets for look up time in O(1).

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

Initiate 3 hash sets using `defaultdict(set)` in pythonto record rows, columns, and boxes separately.
1. Check each numbers and store into set
2. Return `False` if the number has already in set, otherwise return `True`
3. Box index can be note by divide the number by 3 to mark the box from 0 to 2. For instance, box(0,1), (0,2), (1,0)...

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Since the size of the board is fixed, the time and space complexity of this algorithm can be interpreted as O(1).


### HashMap(dictionary) vs HashSet(set): Main Differences

- Purpose:
    - HashMap: HashMap is used to store key-value pairs. It allows you to associate a value with a unique key and retrieve the value based on the key. It provides fast access to values based on their keys.
    - HashSet: HashSet is used to store a collection of unique elements, with no associated values. It ensures that no duplicate elements are present in the set.

- Data Structure:
    - HashMap: HashMap is implemented as a hash table. It uses hashing to map keys to their corresponding values. Each key is unique, and the keys are used to look up the associated values.
    - HashSet: HashSet is also implemented as a hash table, but it stores only the keys (or elements) without associated values. It ensures uniqueness of elements in the set.

- Elements:
    - HashMap: It stores key-value pairs as entries, and the keys must be unique within the HashMap. Values can be duplicated.
    - HashSet: It stores individual elements, and each element must be unique within the set. There are no associated values.

- Access:
    - HashMap: You can access values in a HashMap by providing the corresponding key. It offers efficient key-based lookup operations.
    - HashSet: You can check for the presence of an element in a HashSet using the contains method. It doesn't have a direct key-based lookup, as it's designed for set membership tests.

- Iteration:
    - HashMap: You can iterate through the key-value pairs in a HashMap using methods like keySet, values, or entrySet.
    - HashSet: You can iterate through the elements in a HashSet using an enhanced for loop or an iterator.

- Performance:
    - HashMap: HashMap provides efficient key-based operations and is suitable for situations where you need to associate values with unique keys.
    - HashSet: HashSet is optimized for checking element membership and ensuring uniqueness. It's useful when you only need to store a collection of distinct elements.
