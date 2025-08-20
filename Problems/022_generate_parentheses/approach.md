# 22. Generate Parentheses

**Difficulty:** Medium  
**Topics:** Backtracking  

## Problem

Given `n` pairs of parentheses, generate all **combinations of well-formed parentheses**.

### Examples

**Example 1**  
Input: `n = 3`  
Output: `["((()))","(()())","(())()","()(())","()()()"]`  

**Example 2**  
Input: `n = 1`  
Output: `["()"]`  

---

### Intuition  

- Use **backtracking** to build valid strings character by character.  
- Keep track of **open_count** and **close_count** to ensure parentheses are balanced.  
- Only add `")"` if it won’t violate the balance (`close_count < open_count`).  

---

### Algorithm

1. Initialize an empty list `result` to store all valid combinations.  
2. Define a recursive function `backtrack(current, open_count, close_count)`:
   - If `len(current) == 2 * n`, append `current` to `result`.  
   - If `open_count < n`, recurse with `"("` added and `open_count + 1`.  
   - If `close_count < open_count`, recurse with `")"` added and `close_count + 1`.  
3. Start recursion with `backtrack("", 0, 0)`.  
4. Return `result`.

---

### Complexity

- **Time Complexity:** `O(4^n / sqrt(n))` — number of valid parentheses sequences (Catalan number).  
---