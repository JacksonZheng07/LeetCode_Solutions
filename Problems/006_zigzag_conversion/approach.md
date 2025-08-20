# 6. Zigzag Conversion

**Difficulty:** Medium  
**Topics:** String, Simulation

## Problem 

Given a string `s` and an integer `numRows`, write the string in a zigzag pattern on `numRows` and then read it line by line. Return the resulting string.

### Examples

**Example 1**  
Input: `s = "PAYPALISHIRING"`, `numRows = 3`  
Output: `"PAHNAPLSIIGYIR"`  
Explanation: The zigzag pattern is:  
```
P       A       H       N

A   P   L   S   I   I   G

Y       I       R
```

**Example 2**  
Input: `s = "PAYPALISHIRING"`, `numRows = 4`  
Output: `"PINALSIGYAHRPI"`  
Explanation: The zigzag pattern is:  
```

P           I           N

A       L   S       I   G

Y   A       H   R

P           I
```
**Example 3**  
Input: `s = "A"`, `numRows = 1`  
Output: `"A"`  
Explanation: A single-character string is returned as is.
```
A
```
---

### Intuition  

- Characters are written row by row in a zigzag pattern.  
- The first and last rows only move in one direction, while middle rows alternate between moving down and up.  
- Special handling is needed when `numRows = 1` (return original string) and `numRows = 2` (alternate between two rows).

---

### Algorithm 

1. If `numRows == 1`, return the original string.  
2. Initialize `ListAll` as a list of empty lists (one per row) to store characters.  
3. Initialize `Combine` as an empty string to store the final result.  
4. Track the **current row** and **direction**:  
   - For `numRows = 2`, alternate letters between the two rows.  
   - For `numRows > 2`:  
     - If at the top row, move downward (`descending = True`).  
     - If at the bottom row, move upward (`descending = False`).  
     - Otherwise, move in the current direction.  
5. Append each character to the corresponding row in `ListAll`.  
6. After all characters are placed, combine all rows into a single string `Combine`.  
7. Return `Combine`.

---

### Complexity
- **Time Complexity:** `O(n)` — each character of the input string is visited exactly once.  
