# 9. Palindrome Number

**Difficulty:** Easy  
**Topics:** Math, String

## Problem

Given an integer `x`, return `true` if `x` is a palindrome.  
- An integer is a palindrome when it reads the same backward as forward.

### Examples

**Example 1**  
Input: `x = 121`  
Output: `true`  

**Example 2**  
Input: `x = -121`  
Output: `false`  
Explanation: `-121` reads `121-` backward.  

**Example 3**  
Input: `x = 10`  
Output: `false`  

---

### Intuition  

- Convert the integer to a string to simplify checking.  
- Reverse the string and compare with the original.  
- Palindromes read the same forwards and backwards.

---

### Algorithm (Implemented Approach)
1. Convert integer `x` to string.  
2. Convert string to a list of characters.  
3. Reverse the list.  
4. Reconstruct the reversed string.  
5. Compare the reversed string with the original.  
6. Return `True` if equal, else `False`.

---

### Complexity

- **Time Complexity:** `O(n)` — n = number of digits in `x`.  
---