# 20. Valid Parentheses

**Difficulty:** Easy  
**Topics:** Stack, String  

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.  

- An input string is valid if:
  1. Open brackets are closed by the same type of brackets.
  2. Open brackets are closed in the correct order.

### Examples

**Example 1**  
Input: `s = "()"`  
Output: `True`  

**Example 2**  
Input: `s = "()[]{}"`  
Output: `True`  

**Example 3**  
Input: `s = "(]"`  
Output: `False`  

---

### Intuition  

- Use a **stack** to keep track of opening brackets.  
- Every closing bracket must match the **most recent** opening bracket.  
- If stack is empty at the end, all brackets matched correctly.

---

### Algorithm 

1. Initialize an empty `stack` to track opening brackets.  
2. Create a dictionary `mapping` mapping closing brackets to opening brackets.  
3. Loop through each character in the string:
   - If it is an opening bracket, **push** it onto the stack.
   - If it is a closing bracket:
     - If the stack is empty, return `False`.
     - Pop the top of the stack and check if it matches the closing bracket using `mapping`.
     - If it doesn't match, return `False`.
4. After processing all characters, **return `True` if the stack is empty**, else `False`.

---

### Complexity

- **Time Complexity:** `O(n)` — each character is processed once.  
---