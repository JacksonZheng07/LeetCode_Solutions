# 36. Valid Sudoku

**Difficulty:** Medium  
**Topics:** Hash Table, Backtracking  

## Problem

Determine if a 9x9 Sudoku board is valid.  
Only the **filled cells** need to be validated according to the rules:  
- Each row must contain the digits `1-9` without repetition.  
- Each column must contain the digits `1-9` without repetition.  
- Each of the nine 3x3 sub-boxes must contain the digits `1-9` without repetition.  

### Examples

**Example 1**  
Input:  

```
board =
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
```

Output: `True`

**Example 2**  
Input:  

```
board =
[["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
```


Output: `False`  

---

### Intuition

- Keep track of numbers already seen in **rows**, **columns**, and **3x3 boxes** using sets.  
- Iterate through the board and validate each number.  
- If any repetition occurs in row, column, or box, the board is invalid.  

---

### Algorithm 

1. Initialize three lists of sets: `rows`, `cols`, `boxes`.  
2. Iterate over each cell `(i,j)` in the board:  
   - Skip if the cell is empty `.`.  
   - If the value is in `rows[i]`, `cols[j]`, or `boxes[box_index]`, return `False`.  
   - Otherwise, add the value to the corresponding sets.  
3. Return `True` if no invalid repetitions are found.

---

### Complexity

- **Time Complexity:** `O(1)` — the board is fixed size 9x9.  
---