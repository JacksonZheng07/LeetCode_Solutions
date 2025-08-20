# 32. Longest Valid Parentheses

**Difficulty:** Hard  
**Topics:** Stack, Dynamic Programming  

## Problem

Given a string `s` containing just the characters `'('` and `')'`, find the length of the **longest valid (well-formed) parentheses substring**.

### Examples

**Example 1**  
Input: `s = "(()"`  
Output: `2`  
Explanation: The longest valid parentheses substring is `"()"`.

**Example 2**  
Input: `s = ")()())"`  
Output: `4`  
Explanation: The longest valid parentheses substring is `"()()"`.

**Example 3**  
Input: `s = ""`  
Output: `0`  

---

### Intuition  

- We need a way to track the indices of unmatched parentheses.  
- A stack can store indices:
  - Push index of `'('`.
  - For `')'`, pop the stack.
- Use the difference between current index and last unmatched index to calculate valid substring length.

---

### Algorithm 

1. Initialize `stack = [-1]` and `max_len = 0`.  
2. Loop through the string `s` with index `i`:
   - If `s[i] == '('`, push `i` onto `stack`.  
   - Else:
     - Pop the stack.  
     - If stack becomes empty, push `i` as the new base.  
     - Otherwise, update `max_len = max(max_len, i - stack[-1])`.  
3. Return `max_len`.

---

### Complexity

- **Time Complexity:** `O(n)` — each index is pushed and popped at most once.  
---